from django.db import models


class TrackedItem(models.Model):
    url = models.URLField(unique=True)
    name = models.CharField(max_length=255)
    current_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0.0
    )
    lowest_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0.0
    )
    last_checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PriceHistory(models.Model):
    item = models.ForeignKey(
        TrackedItem, on_delete=models.CASCADE, related_name="price_history"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} - {self.price} at {self.timestamp}"

    class Meta:
        ordering = ["timestamp"]  # Ensures the data is always ordered by time
