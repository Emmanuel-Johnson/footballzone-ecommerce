from django.shortcuts import render


def about(request):
    return render(request, "users/core/about.html")


def contact(request):
    return render(request, "users/core/contact.html")


def page_not_found(request):
    return render(request, "users/core/page_not_found.html")
