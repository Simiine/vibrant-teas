from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
]


# urlpatterns = [
#     # path('', views.all_reviews, name='reviews'),
#     path('delete_review/<int:review_id>/', views.DeleteReview.as_view(), name='delete_review'),
#     path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
#     path('product/<product_id>/delete/<review_id>/', views.DeleteReview.as_view(), name='delete_review')

#     path('delete_review/<int:pk>', views.ExperienceDeleteComment.as_view(), name='delete_comment'),
# ]