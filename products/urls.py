from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('<accessories_id>', views.accessories_detail, name='accessories_detail'),
]