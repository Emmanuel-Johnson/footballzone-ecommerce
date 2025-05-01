from django.urls import path
from . import views

urlpatterns = [
    path("login-register/", views.login_register, name="login_register"),
    path("user-profile/", views.user_profile, name="user_profile"),
]
