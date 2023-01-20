from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Model for Reviews
    """
    class Meta:
        model = Review
        fields = ('review_text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# class ReviewForm(forms.ModelForm):
#     """
#     Model to Add / Edit Review
#     """
#     class Meta:
#         model = Product
#         fields = ('rating', 'review_text')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)