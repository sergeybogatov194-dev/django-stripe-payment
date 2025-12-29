from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from apps.orders.models import Order
from .services import create_checkout_session
import stripe


@login_required
def payment_order(request):
    order = get_object_or_404(Order, user=request.user, payment_status="PENDING")
    session = create_checkout_session(order)
    order.stripe_session_id = session.id
    order.save()
    return JsonResponse({
        "session_id": session.id
    })


def success_view(request):
    session_id = request.GET.get("session_id")
    session = stripe.checkout.Session.retrieve(session_id)
    if session.payment_status == "paid":
        order = get_object_or_404(
            Order,
            stripe_session_id=session_id
        )
        order.payment_status = "SUCCESSFUL"
        order.save()
        return render(request, "payments/success.html")
    else:
        return render(request, "payments/cancel.html")


def cancel_view(request):
    return render(request, "payments/cancel.html")