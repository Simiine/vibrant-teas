from django.shortcuts import render
from .models import Product, Accessories

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    accessories = Accessories.objects.all()

    context = {
        'products': products,
        'accessories': accessories,
    }

    return render(request, 'products/products.html', context)