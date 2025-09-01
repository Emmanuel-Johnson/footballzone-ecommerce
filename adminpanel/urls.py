from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", lambda request: redirect("login")),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path("users-list/", views.users_list, name="users_list"),
    path("user-details/<int:user_id>", views.user_details, name="user_details"),
    path("user-add/", views.user_add, name="user_add"),
    path("user-address-add/", views.user_address_add, name="user_address_add"),
    path("user-block/<int:user_id>", views.user_block, name="user_block"),
    path('admin/add-address/', views.admin_add_address, name='admin_add_address'),

    path("categories-list/", views.categories_list, name="categories_list"),
    path("category-edit/", views.category_edit, name="category_edit"),

    path("products-list/", views.products_list, name="products_list"),
    path("product-add/", views.product_add, name="product_add"),
    path("product-edit/", views.product_edit, name="product_edit"),
]
