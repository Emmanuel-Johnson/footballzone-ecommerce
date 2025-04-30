from django.shortcuts import render


def cart(request):
    return render(request, "users/orders/cart.html")


def checkout(request):
    return render(request, "users/orders/checkout.html")
