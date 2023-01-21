from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('product', 'rating', 'review_text', 'date', 'user')
    list_filter = ('product', 'rating', 'date')

admin.site.register(Review, ReviewAdmin)

