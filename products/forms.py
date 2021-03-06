from django import forms
from .widgets import (
    CustomImageClearableFileInput,
    CustomAudioClearableFileInput)
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomImageClearableFileInput)

    audio = forms.FileField(
        label='Audio', required=False, widget=CustomAudioClearableFileInput)

    def __init__(self, *args, **kwargs):  # pragma: no cover
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-white rounded-0'
