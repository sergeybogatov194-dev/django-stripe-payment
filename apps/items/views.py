from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Item
from ..orders.models import Order, OrderItem
from ..pricing.models import Discount, Tax


def home(request):
    items = Item.objects.all()
    return render(request, "home.html", {"items": items})

@login_required
def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(
        request,
        "item_detail.html",
        context={"item": item, "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY,}
    )

@login_required
def add_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    zero_discount = Discount.objects.get_or_create(
        name="No discount",
        defaults={"percentage": 0}
    )[0]
    zero_tax = Tax.objects.get_or_create(
        name="No tax",
        defaults={"percentage": 0}
    )[0]
    order, _ = Order.objects.get_or_create(
        user=request.user,
        payment_status="PENDING",
        defaults={"discount": zero_discount, "tax": zero_tax}
    )
    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        item=item,
        defaults={"quantity": 1}
    )

    if not created:
        order_item.quantity += 1
        order_item.save()
    return redirect("home")