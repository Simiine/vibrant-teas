from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Accessories, Category, Subcategory
from django.db.models.functions import Lower

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    accessory = Accessories.objects.all()
    query = None
    categories = None
    subcategories = None
    sort = None
    direction = None
    

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                accessory = accessory.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            accessory = accessory.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            accessory = accessory.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'subcategory' in request.GET:
            subcategories = request.GET['subcategory'].split(',')
            products = products.filter(subcategory__name__in=subcategories)
            accessory = accessory.filter(subcategory__name__in=subcategories)
            subcategories = Subcategory.objects.filter(name__in=subcategories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
                return redirect(reverse('accessory'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            accessory = accessory.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_subcategories': subcategories,
        'current_sorting': current_sorting,
        'accessory': accessory,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def accessories_detail(request, accessories_id):
    """ A view to show individual accessories details """

    accessories = get_object_or_404(Accessories, pk=accessories_id)

    context = {
        'accessories': accessories,
    }

    return render(request, 'accessory/accessories_detail.html', context)