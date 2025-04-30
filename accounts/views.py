from django.shortcuts import render


def register_login(request):
    return render(request, "users/accounts/register_login.html")


def user_profile(request):
    return render(request, "users/accounts/user_profile.html")
