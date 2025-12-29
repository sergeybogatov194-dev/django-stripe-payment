from django.conf import settings
from django.db import models
from apps.items.models import Item
from apps.pricing.models import Discount, Tax

PAYMENT_STATUS_CHOICES = (
    ("PENDING", "PENDING"),
    ("PROCESSING", "PROCESSING"),
    ("SUCCESSFUL", "SUCCESSFUL"),
    ("CANCELLED", "CANCELLED"),
    ("FAILED", "FAILED"),
)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_status = models.CharField(
        max_length=20,
        default="PENDING",
        choices=PAYMENT_STATUS_CHOICES
    )
    discount = models.ForeignKey(Discount, on_delete=models.SET_DEFAULT, null=True, blank=True, default=1)
    tax = models.ForeignKey(Tax, on_delete=models.SET_DEFAULT, null=True, blank=True, default=1)
    stripe_session_id = models.CharField(max_length=255, blank=True, null=True)

    @property
    def total_cost_order(self):
        order_items = self.items.all()
        total = sum([prod.total_cost_item for prod in order_items])
        return total

    @property
    def count_items(self):
        order_items = self.items.all()
        return sum([prod.quantity for prod in order_items])

    def __str__(self):
        return f"{self.user.username}`s order"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost_item(self):
        return self.item.price * self.quantity

    def __str__(self):
        return self.item.name