from django.contrib import admin
from .models import Producer

class ProducerAdmin(admin.ModelAdmin):
    """
    Admin settings to display list of Producers
    """
    list_display = ('name', 'location')
    ordering = ('location',)

admin.site.register(Producer, ProducerAdmin)

# class ProducerAdmin(admin.ModelAdmin):
#     """
#     Admin settings to display list of Producers
#     """

#     model = Producer
#     list_display = ("name", "location")
#     ordering = ("location",)