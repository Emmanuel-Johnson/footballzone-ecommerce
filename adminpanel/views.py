from django.shortcuts import render, redirect
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from accounts.models import Account 

def login(request):
    return render(request, "admin/accounts/login.html")


def dashboard(request):
    return render(request, "admin/dashboard/home.html")


def users_list(request):
    users = Account.objects.filter(is_superuser=False, is_staff=False).order_by('id')
    return render(request, "admin/users/list.html", {"users": users})


def user_add(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        password = "defaultpassword123" 

        if Account.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            user = Account.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number
            )
            messages.success(request, f"User {email} added successfully")

        return redirect("user_add")  
    return render(request, "admin/users/add.html")


def user_block(request, user_id):
    user = get_object_or_404(Account, id=user_id)
    
    user.is_active = not user.is_active
    user.save()

    if user.is_active:
        messages.success(request, f"{user.email} has been activated.")
    else:
        messages.warning(request, f"{user.email} has been blocked.")
    
    return redirect('users_list') 


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