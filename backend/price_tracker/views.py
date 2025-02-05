from collections import defaultdict
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import PriceHistory, TrackedItem, ItemResult
from .forms import TrackedItemForm
from .scraper import LazadaScraper  # Import the scraper
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
import json


@api_view(["GET"])
def get_csrf_token(request):
    return Response({"csrfToken": get_token(request)})


@csrf_exempt
def add_tracked_item(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            url = data.get("url")

            if not url:
                return JsonResponse({"error": "URL is required"}, status=400)

            scraper = LazadaScraper()
            name, price = scraper.find_price_and_name(url)
            scraper.close()

            if name and price:
                price = float(price.replace("฿", "").replace(",", "").strip())
                tracked_item, created = TrackedItem.objects.get_or_create(url=url)
                ItemResult.objects.create(url=url, name=name, current_price=price)

                return JsonResponse({"message": "Item tracked successfully"})
            else:
                return JsonResponse(
                    {"error": "Unable to scrape item information"}, status=400
                )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)


def show_all_items(request):
    items = TrackedItem.objects.all()
    results = ItemResult.objects.all()
    joined_data = []

    for item in items:
        result = results.filter(url=item.url).order_by("-created_at").first()
        if result:
            joined_data.append(
                {
                    "tracked_id": item.id,
                    "url": item.url,
                    "name": result.name,
                    "current_price": result.current_price,
                    "created_at": result.created_at,
                    "tracked": item.tracked,
                }
            )

    return JsonResponse({"items": joined_data}, safe=False)

def show_all_history(request):
    items = TrackedItem.objects.all()
    results = ItemResult.objects.all().order_by("-created_at")  # Order by newest first

    # Dictionary to group results by URL
    history_data = defaultdict(list)
    
    for result in results:
        history_data[result.url].append(
            {
                "name": result.name,
                "current_price": float(result.current_price),
                "created_at": result.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    joined_data = []
    for item in items:
        if item.url in history_data:
            joined_data.append(
                {
                    "tracked_id": item.id,
                    "url": item.url,
                    "name": history_data[item.url][0]["name"],  # Latest name
                    "price_history": history_data[item.url],
                }
            )

    return JsonResponse({"items": joined_data}, safe=False)

@csrf_exempt
def update_tracked_prices(request):
    if request.method == "POST":
        try:
            items = TrackedItem.objects.filter(tracked=True)
            scraper = LazadaScraper()
            updated_items = []

            for item in items:
                name, price = scraper.find_price_and_name(item.url)
                if name and price:
                    price = float(price.replace("฿", "").replace(",", "").strip())
                    ItemResult.objects.create(
                        url=item.url, name=name, current_price=price
                    )
                    updated_items.append({"name": name, "new_price": price})

            scraper.close()
            return JsonResponse(
                {"message": "Tracked prices updated", "updated_items": updated_items}
            )

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)


def tracked_items(request):
    items = TrackedItem.objects.all()
    return render(request, "tracker/tracked_items.html", {"items": items})


def item_detail(request, item_id):
    item = TrackedItem.objects.get(id=item_id)
    price_history = ItemResult.objects.filter(url=item.url).order_by("-created_at")
    return render(
        request,
        "tracker/item_detail.html",
        {"item": item, "price_history": price_history},
    )
