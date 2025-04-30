from django.shortcuts import render


def login(request):
    return render(request, "admin/accounts/login.html")


def dashboard(request):
    return render(request, "admin/dashboard/home.html")


def users(request):
    return render(request, "admin/users/list.html")


def categories(request):
    return render(request, "admin/categories/list.html")


def products(request):
    return render(request, "admin/products/list.html")
