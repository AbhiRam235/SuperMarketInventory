from django.shortcuts import render, get_object_or_404
from django.db.models import F, ExpressionWrapper, DecimalField
from collections import defaultdict
from .models import Product, Category

def product_detail(request, username, category, subcategory, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, "product_detail.html", {
        "product": product,
        "category": product.subcategory.category if product.subcategory else None,
        "subcategory": product.subcategory if product.subcategory else None,
    })

def deals_page(request):
    # Calculate the discounted price dynamically
    discounted_price = ExpressionWrapper(
        F('price') - (F('price') * F('discount') / 100),
        output_field=DecimalField(max_digits=10, decimal_places=2)
    )

    # Fetch products that have discounts and stock available
    deals = Product.objects.annotate(discounted_price=discounted_price).filter(
        discount__gt=0,  # Only include products that have a discount
        stock_quantity__gt=0  # Only include available products
    ).select_related('subcategory', 'subcategory__category')  # Optimize query

    # Group products by category and subcategory
    categorized_deals = defaultdict(lambda: defaultdict(list))

    for product in deals:
        category_name = product.subcategory.category.name
        subcategory_name = product.subcategory.name
        categorized_deals[category_name][subcategory_name].append({
            "id": product.id,
            "name": product.name,
            "image": product.image.url if product.image else None,
            "price": str(product.price),  # Convert Decimal to string
            "discounted_price": str(product.discounted_price),  # Convert Decimal to string
            "discount": str(product.discount),  # Convert Decimal to string
        })

    return render(request, 'deals.html', {
    'categorized_deals': dict(categorized_deals),
    'username': request.user.username if request.user.is_authenticated else "guest",
})
