from django.db import models
from django.template.defaultfilters import slugify
from producers.models import Producer


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

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory', null=True,
                                    blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    producer = models.ForeignKey(Producer, blank=True, null=True,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True, null=False)
    description = models.TextField()
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
