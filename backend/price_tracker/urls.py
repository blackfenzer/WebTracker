from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_tracked_item, name="add_tracked_item"),
    path("", views.tracked_items, name="tracked_items"),
    path("item/<int:item_id>/", views.item_detail, name="item_detail"),
    path("csrf_token/", views.get_csrf_token, name="csrf_token"),
    # path("show/", views.show_all_items, name="show"),
    path("update/", views.update_tracked_prices, name="update"),
    path("show/", views.show_all_items, name="show_all_items"),
    path("history/", views.show_all_history, name="show_all_history"),
    path("all/", views.scrape_all_items, name="scrape_all_items"),
]

# use show ,history ,add , scrape_all
