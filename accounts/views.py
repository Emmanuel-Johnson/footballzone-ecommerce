from django.shortcuts import render


def login_register(request):
    return render(request, "users/accounts/login_register.html")


def user_profile(request):
    return render(request, "users/accounts/user_profile.html")
