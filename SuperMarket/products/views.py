from django.shortcuts import render, get_object_or_404
from django.db.models import F, ExpressionWrapper, DecimalField
from collections import defaultdict
from .models import Product, Category
from users.models import User

def product_detail(request, username, category, subcategory, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, "product_detail.html", {
        "product": product,
        "category": product.subcategory.category if product.subcategory else None,
        "subcategory": product.subcategory if product.subcategory else None,
    })

def deals_page(request):
    user_id = request.session.get("user_id")

    user = User.objects.get(id=user_id)  # Get user from database
    categories = Category.objects.all()  # Fetch all categories
    products = Product.objects.select_related("category", "subcategory").all()  # Optimize query

    # Calculate the discounted price for each product
    for product in products:
        product.discounted_price = round(product.price - (product.price * product.discount / 100), 2)

    return render(request, "deals.html", {
        "user": user,
        "username": user.name,  # Explicitly pass username
        "categories": categories,
        "products": products
    })
