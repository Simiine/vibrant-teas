from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from profiles.models import UserProfile

from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """
    Add a review for a product
    """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.rating = int(request.POST.get('ratings'))
            review.user = user
            review.product = product
            review.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = ReviewForm()
        
    template = 'reviews/add_review.html'
    context = {
        'product': product,
        'form': form,
        'user_profile': user,
    }

    return render(request, template, context)

@login_required
def edit_review(request, review_id):
    """
    Edit a review for a product
    """
    review = get_object_or_404(Review, pk=review_id)
    user = get_object_or_404(UserProfile, user=request.user)
    product = review.product

    if not request.user != review.user:
        messages.error(request, 'You can only edit your own review')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.rating = int(request.POST.get('ratings'))
            review.user = user
            review.product = product
            review.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.product.name}')

    template = 'reviews/edit_review.html'
    context = {
        'review': review,
        'product': product,
        'form': form,
        'user_profile': user,
    }

    return render(request, template, context)

@login_required
def delete_review(request, review_id):
    """
    Delete a review for a product
    """
        
    review = get_object_or_404(Review, pk=review_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if not request.user != review.user:
        messages.error(request, 'You can only delete your own review')
        return redirect(reverse('home'))

    review.delete()
    messages.success(request, 'Review Sucessfully deleted!')

    return redirect(reverse('product_detail', args=[review.product.id]))
