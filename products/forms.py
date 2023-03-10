from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Subcategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'subcategory', 'sku', 'producer',
                  'name', 'description', 'weight', 'price',
                  'image_url', 'image')

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        friendly_names_cat = [
            (c.id, c.get_friendly_name()) for c in categories]

        subcategories = Subcategory.objects.all()
        friendly_names_sub = [
            (s.id, s.get_friendly_name()) for s in subcategories]

        self.fields['category'].choices = friendly_names_cat
        self.fields['subcategory'].choices = friendly_names_sub
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
