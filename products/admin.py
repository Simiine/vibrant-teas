from django.contrib import admin
from .models import Product, Category, Subcategory

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'subcategory',
        'price',
        'weight',
        'image',
    )

    ordering = ('sku',)

# class AccessoriesAdmin(admin.ModelAdmin):
#     list_display = (
#         'sku',
#         'name',
#         'category',
#         'subcategory',
#         'price',
#         'image',
#     )

#     ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
# admin.site.register(Accessories, AccessoriesAdmin)
