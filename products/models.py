from django.db import models
from django.template.defaultfilters import slugify
# from producers.models import Producer

class Category(models.Model):
    """
    Class for the category model
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Subcategory(models.Model):
    """ 
    Class for subcategory model
    """
    class Meta:
        verbose_name_plural = 'Subcategories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    """
    Class for the product model
    """
    # WEIGHTS = [(100), (200), (500),]

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    # producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=False)
    description = models.TextField()
    # weight = models.IntegerField(blank=True, null=True)
    # weight = models.IntegerField(choices=WEIGHTS, help_text='in grams', null=False, blank=False)
    # weight = models.PositiveIntegerField(help_text='in grams', blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True, default="500")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

# class Accessories(models.Model):
#     """
#     Class for the accessories model
#     """
#     category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
#     subcategory = models.ForeignKey('Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
#     sku = models.CharField(max_length=254, null=True, blank=True)
#     name = models.CharField(max_length=254)
#     slug = models.SlugField(max_length=200, unique=True, blank=True, null=False)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image_url = models.URLField(max_length=1024, null=True, blank=True)
#     image = models.ImageField(null=True, blank=True)

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         return super().save(*args, **kwargs)

# class Review(models.Model):
#     """
#     Model for product review
#     """
#     product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, related_name="reviews")
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_reviews')
#     review = models.TextField(max_length=1000)
#     created_on = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)
    
#     class Meta:
#         """
#         Order reviews in ascending order
#         """
#         ordering = ['created_on']

#     def __str__(self):
#         """
#         Return string representation
#         """
#         return f"Review {self.review} by {self.author}"