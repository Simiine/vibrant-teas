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

