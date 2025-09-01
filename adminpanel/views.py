from django.shortcuts import render, redirect
from django.shortcuts import redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from accounts.models import Account, Address
from django.http import JsonResponse


def login(request):
    return render(request, "admin/accounts/login.html")


def dashboard(request):
    return render(request, "admin/dashboard/home.html")


def users_list(request):
    users = Account.objects.filter(is_superuser=False, is_staff=False).order_by('id')
    user_data = request.GET.get('username')

    if user_data:
        users = users.filter(
            Q(first_name__icontains=user_data) |
            Q(last_name__icontains=user_data) 
        )

    status = request.GET.get('status')
    if status == 'active':
        users = users.filter(is_active=True)
    elif status == 'inactive':
        users = users.filter(is_active=False)

    paginator = Paginator(users, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "users": page_obj,  
    }
    return render(request, "admin/users/list.html", context)


def user_details(request, user_id):
    user = get_object_or_404(Account, id=user_id)
    return render(request, "admin/users/details.html", {"user": user})




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


def user_address_add(request):
    return render(request, "admin/users/address.html")

def user_block(request, user_id):
    if request.method == "POST":
        user = get_object_or_404(Account, id=user_id)
        user.is_active = not user.is_active
        user.save()
        return JsonResponse({
            "success": True,
            "new_status": "active" if user.is_active else "inactive"
        })
    return JsonResponse({"success": False}, status=400)



def admin_add_address(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')  # you need to send user id if adding for a specific user
        user = Account.objects.get(id=user_id)  # get the user

        try:
            address = Address.objects.create(
                user=user,
                name=request.POST.get('name'),
                phone=request.POST.get('phone'),
                alt_phone=request.POST.get('alt_phone'),
                pincode=request.POST.get('pincode'),
                locality=request.POST.get('locality'),
                address=request.POST.get('address'),
                city=request.POST.get('city'),
                state=request.POST.get('state'),
                landmark=request.POST.get('landmark'),
                address_type=request.POST.get('address_type')
            )
            return JsonResponse({'success': True, 'address': f"{address.name}, {address.address}, {address.city}"})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request'})


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