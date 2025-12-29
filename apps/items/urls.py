from django.urls import path
from apps.items import views

urlpatterns = [
    path("<str:item_id>/", views.item_detail),
    path("cart/add/<str:item_id>/", views.add_item, name="add_item"),
]