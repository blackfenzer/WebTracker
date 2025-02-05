from django.db import models


class ItemResult(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(unique=False)
    name = models.CharField(max_length=255)
    current_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0.0
    )
    rating = models.IntegerField(null=False, default=0)
    # lowest_price = models.DecimalField(
    #     max_digits=10, decimal_places=2, null=False, default=0.0
    # )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TrackedItem(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(unique=True)
    # name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    tracked = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PriceHistory(models.Model):
    item = models.ForeignKey(
        TrackedItem, related_name="price_history", on_delete=models.CASCADE
    )
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} - {self.price} at {self.timestamp}"
