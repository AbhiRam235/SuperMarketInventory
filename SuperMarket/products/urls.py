from django.urls import path
from .views import product_detail, deals_page

urlpatterns = [
    path("<str:username>/<slug:category>/<slug:subcategory>/<int:product_id>/", product_detail, name="product_detail"),
    path('deals/', deals_page, name='deals'),
]
