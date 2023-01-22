from django.db import models

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):
    """
    Model for review
    """
    RATINGS = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),]

    rating = models.IntegerField(choices=RATINGS)
    user = models.ForeignKey(UserProfile, null=False,
                             blank=False, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, null=False,
                                blank=False, on_delete=models.CASCADE)

    class Meta:
        """
        Order reviews in ascending order
        """
        ordering = ['date']

    def __str__(self):
        """
        Return string representation
        """
        return f"Review {self.review_text} by {self.user}"
