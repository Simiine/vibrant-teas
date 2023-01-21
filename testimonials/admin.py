from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    """
    Admin settings to display list of Producers
    """
    list_display = ('name', 'rating', 'details')


admin.site.register(Testimonial, TestimonialAdmin)
