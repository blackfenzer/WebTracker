from rest_framework import serializers
from .models import TrackedItem, PriceHistory


# class PriceHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PriceHistory
#         fields = ["id", "price", "timestamp"]


# class TrackedItemSerializer(serializers.ModelSerializer):
#     price_history = PriceHistorySerializer(
#         many=True, read_only=True, source="pricehistory_set"
#     )

#     class Meta:
#         model = TrackedItem
#         fields = [
#             "id",
#             "url",
#             "name",
#             "current_price",
#             "lowest_price",
#             "last_checked",
#             "price_history",
#         ]


# class ItemTrackRequestSerializer(serializers.Serializer):
#     url = serializers.URLField()
