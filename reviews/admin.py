from django.contrib import admin
from .models import Review


# class ReviewAdmin(admin.ModelAdmin):
#     model = Review
#     list_display = ('rating', 'review_text', 'created_on', 'user')
#     list_filter = ('rating', 'created_on')

# admin.site.register(Review, ReviewAdmin)

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('product', 'rating', 'review_text', 'date', 'user')
    list_filter = ('product', 'rating', 'date')

admin.site.register(Review, ReviewAdmin)


# class ReviewAdmin(admin.ModelAdmin):
#     """
#     Admin settings to display list of Reviews
#     """

#     model = Review
#     list_display = ('product', 'date', 'user', 'rating', 'review_text',)

#     ordering = ('-product', '-date')
#     list_filter = ('rating',)


# admin.site.register(Review, ReviewAdmin)
