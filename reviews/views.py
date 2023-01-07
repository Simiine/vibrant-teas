from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from profiles.models import UserProfile

from .models import Review
from .forms import ReviewForm

def all_reviews(request):
    """ A view to show all reviews """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'reviews/reviews.html', context)

@login_required
def add_review(request, product_id):
    """ Add a product review """
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()
        
    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_review(request, product_id):
    """ Edit a product review """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'reviews/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_review(request, product_id):
    """ Delete a product review """        
    product = get_object_or_404(Product, pk=product_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('products'))
