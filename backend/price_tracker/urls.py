from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_tracked_item, name="add_tracked_item"),
    path("", views.tracked_items, name="tracked_items"),
    path("item/<int:item_id>/", views.item_detail, name="item_detail"),
    path("csrf_token/", views.get_csrf_token, name="csrf_token"),
    path("show/", views.show_all_items, name="show"),
]
