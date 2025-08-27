from django.shortcuts import render


def login(request):
    return render(request, "admin/accounts/login.html")


def dashboard(request):
    return render(request, "admin/dashboard/home.html")


def users_list(request):
    return render(request, "admin/users/list.html")


def user_add(request):
    return render(request, "admin/users/add.html")


def categories_list(request):
    return render(request, "admin/categories/list.html")


def category_edit(request):
    return render(request, "admin/categories/edit.html")


def products_list(request):
    return render(request, "admin/products/list.html")


def product_add(request):
    return render(request, "admin/products/add.html")


def product_edit(request):
    return render(request, "admin/products/edit.html")