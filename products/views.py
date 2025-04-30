from django.shortcuts import render


def home(request):
    return render(request, "users/products/home.html")


def shop(request):
    return render(request, "users/products/shop.html")


def product_details(request):
    return render(request, "users/products/product_details.html")


def wishlist(request):
    return render(request, "users/products/wishlist.html")
