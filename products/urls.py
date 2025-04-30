from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("product-details/", views.product_details, name="product_details"),
    path("wishlist/", views.wishlist, name="wishlist"),
]
