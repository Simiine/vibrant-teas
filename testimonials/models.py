from django.db import models

class Testimonial(models.Model):
    """
    Class for the testimonials model
    """

    RATINGS = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),]

    rating = models.IntegerField(choices=RATINGS)
    name = models.CharField(max_length=256)
    details = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
