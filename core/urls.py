from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("page_not_found/", views.page_not_found, name="page_not_found"),
]
