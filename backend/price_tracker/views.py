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


def add_tracked_item(request):
    if request.method == "POST":
        form = TrackedItemForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
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

                return redirect("tracked_items")
    else:
        form = TrackedItemForm()
    return render(request, "tracker/add_tracked_item.html", {"form": form})


def tracked_items(request):
    items = TrackedItem.objects.all()
    return render(request, "tracker/tracked_items.html", {"items": items})


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
