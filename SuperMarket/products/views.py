from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, username, category, subcategory, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, "product_detail.html", {
        "product": product,
        "category": product.subcategory.category if product.subcategory else None,
        "subcategory": product.subcategory if product.subcategory else None,
    })
