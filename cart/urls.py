from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_detail, name="detail"),
    path("add/<int:product_id>/", views.add_to_cart, name="add"),
    path("remove/<int:product_id>/", views.remove_from_cart, name="remove"),
]
