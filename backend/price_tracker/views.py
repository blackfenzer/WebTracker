from django.shortcuts import render, redirect
from django.utils import timezone
from .models import TrackedItem, PriceHistory
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

@csrf_exempt
def add_tracked_item(request):
    if request.method == "POST":
        try:
            # Parse the JSON body
            data = json.loads(request.body.decode("utf-8"))
            url = data.get("url")

            if not url:
                return JsonResponse({"error": "URL is required"}, status=400)

            scraper = LazadaScraper()
            name, price = scraper.find_price_and_name(url)
            scraper.close()

            if name and price:
                # Convert price to a decimal (remove currency symbols, etc.)
                price = float(price.replace("฿", "").replace(",", "").strip())

                # Create or update the TrackedItem
                item, created = TrackedItem.objects.get_or_create(url=url)
                item.name = name
                item.current_price = price
                if created or price < item.lowest_price:
                    item.lowest_price = price
                item.save()

                # Add price to PriceHistory
                PriceHistory.objects.create(item=item, price=price)

                return JsonResponse({"message": "Item added successfully"})
            else:
                return JsonResponse(
                    {"error": "Unable to scrape item information"}, status=400
                )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)


def tracked_items(request):
    items = TrackedItem.objects.all()
    return render(request, "tracker/tracked_items.html", {"items": items})


def show_all_items(request):
    items = TrackedItem.objects.all()
    items_data = [
        {
            "id": item.id,
            "name": item.name,
            "url": item.url,
            "current_price": item.current_price,
            "lowest_price": item.lowest_price,
            "last_checked": item.last_checked,
        }
        for item in items
    ]
    return JsonResponse({"items": items_data}, safe=False)


def item_detail(request, item_id):
    item = TrackedItem.objects.get(id=item_id)
    price_history = item.price_history.all()
    return render(
        request,
        "tracker/item_detail.html",
        {"item": item, "price_history": price_history},
    )


@api_view(["GET"])
def get_csrf_token(request):
    return Response({"csrfToken": get_token(request)})
