from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from profiles.models import UserProfile

from .models import Review
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    """ Add a review for a product """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
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
    """ Edit a review for a product """
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
    """ Delete a review for a product """
        
    review = get_object_or_404(Review, pk=review_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if not request.user != review.user:
        messages.error(request, 'You can only delete your own review')
        return redirect(reverse('home'))

    review.delete()
    messages.success(request, 'Review Sucessfully deleted!')

    template = 'reviews/delete_review.html'

    return redirect(reverse('product_detail', args=[review.product.id]))

# class DeleteReview(DeleteView):
#     """
#     Delete review
#     """
#     model = Review
#     template_name = 'delete_review.html'
#     success_url = reverse_lazy('products')

# @login_required
# def delete_review(request, review_id):
#     """ View to delete a review """

#     review = get_object_or_404(Review, pk=review_id)
#     user = get_object_or_404(UserProfile, user=request.user)
#     product = review.product
#     deleted_rating = review.rating
#     total_product_reviews = Review.objects.filter(
#         product=product.id).count() + 1


#     product.save()

#     review.delete()

#     messages.add_message(
#         request,
#         SUCCESS_NO_BAG,
#         'Review successfully deleted!'
#     )
#     return redirect(reverse('product_detail', args=[review.product.id]))

# def all_reviews(request):
#     """ A view to show all reviews """
#     product = get_object_or_404(Product, pk=product_id)

#     context = {
#         'product': product,
#     }

#     return render(request, 'reviews/reviews.html', context)

# @login_required
# def add_review(request, product_id):
#     """ Add a product review """
#     if request.method == 'POST':
#         form = ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             review = form.save()
#             messages.success(request, 'Successfully added review!')
#             return redirect(reverse('product_detail', args=[product.id]))
#         else:
#             messages.error(request, 'Failed to add review. Please ensure the form is valid.')
#     else:
#         form = ReviewForm()
        
#     template = 'reviews/add_review.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)

# @login_required
# def edit_review(request, product_id):
#     """ Edit a product review """
#     product = get_object_or_404(Product, pk=product_id)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Successfully updated review!')
#             return redirect(reverse('product_detail', args=[product.id]))
#         else:
#             messages.error(request, 'Failed to update review. Please ensure the form is valid.')
#     else:
#         form = ProductForm(instance=product)
#         messages.info(request, f'You are editing {product.name}')

#     template = 'reviews/edit_product.html'
#     context = {
#         'form': form,
#         'product': product,
#     }

#     return render(request, template, context)

# @login_required
# def delete_review(request, product_id):
#     """ Delete a product review """        
#     product = get_object_or_404(Product, pk=product_id)
#     review.delete()
#     messages.success(request, 'Review deleted!')
#     return redirect(reverse('products'))
