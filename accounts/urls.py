from django.urls import path
from . import views

urlpatterns = [
    path("register-login/", views.register_login, name="register_login"),
    path("user-profile/", views.user_profile, name="user_profile"),
]
