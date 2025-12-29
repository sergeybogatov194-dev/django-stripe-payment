from django.urls import path
from apps.payments import views

urlpatterns = [
    path("buy/", views.payment_order, name="payment_order"),
    path("success/", views.success_view, name="success"),
    path("cancel/", views.cancel_view, name="cancel"),
]