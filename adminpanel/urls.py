from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", lambda request: redirect("login")),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("users-list/", views.users, name="users_list"),
    path("categories-list/", views.categories, name="categories_list"),
    path("products-list/", views.products, name="products_list"),
]
