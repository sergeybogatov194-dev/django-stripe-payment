from django.urls import path
from apps.orders import views

urlpatterns = [
    path("cart/", views.cart, name="cart")
]