from django.urls import path
from .views import product_detail

urlpatterns = [
    path("<str:username>/<slug:category>/<slug:subcategory>/<int:product_id>/", product_detail, name="product_detail"),
]
