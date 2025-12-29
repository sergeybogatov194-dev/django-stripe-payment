from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Order
from django.conf import settings

@login_required
def cart(request):
    order = Order.objects.filter(
        user=request.user,
        payment_status="PENDING"
    ).first()
    if not order:
        messages.info(
            request,
            "У вас пока нет заказов. Добавьте хотя бы один товар в корзину."
        )
        return redirect("home")
    return render(request, "cart.html", {"order": order, "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY})
