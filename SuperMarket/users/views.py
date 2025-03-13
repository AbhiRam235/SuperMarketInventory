from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from .models import User
from products.models import Product, Category, SubCategory
from django.contrib import messages
from django.contrib.auth.hashers import check_password

def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, "register.html", {"form": form})

            user = form.save(commit=False)  # Get form data without saving yet
            user.save()  # Save user instance

            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")
        else:
            messages.error(request, "Error in registration. Please check your details.")
    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email_or_phone = form.cleaned_data['email_or_phone']
            password = form.cleaned_data['password']

            # Check if user exists by email or phone
            user = User.objects.filter(email=email_or_phone).first() or User.objects.filter(phone=email_or_phone).first()

            if user and check_password(password, user.password):
                request.session['user_id'] = user.id  # Store user ID in session
                request.session['role'] = user.role   # Store user role in session

                # Redirect users based on role
                role_redirects = {
                    "owner": "owner_dashboard",
                    "customer": "customer_dashboard",
                    "staff": "staff_dashboard",
                    "delivery": "delivery_dashboard",
                }
                return redirect(role_redirects.get(user.role, "login"))

            messages.error(request, "Invalid email/phone or password. Please try again.")

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})

def profile(request):
    # Fetch user from session
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")  # Redirect to login if session expired

    user = User.objects.get(id=user_id)  # Get the user from DB

    if request.method == "POST":
        # Update user details
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.phone = request.POST.get("phone")
        user.address = request.POST.get("address")
        user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("profile")

    return render(request, "profile.html", {"user": user})

def owner_dashboard(request):
    return render(request, "owner_dashboard.html")


def customer_dashboard(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")  # Redirect to login if session expired

    user = User.objects.get(id=user_id)  # Get user from database
    categories = Category.objects.all()  # Fetch all categories
    products = Product.objects.select_related("category", "subcategory").all()  # Optimize query

    return render(request, "customer_dashboard.html", {
        "user": user,
        "username": user.name,  # Explicitly pass username
        "categories": categories,
        "products": products
    })


def home(request):
    return render(request, "partials/home.html")


def logout_view(request):
    request.session.flush()
    return redirect("home")