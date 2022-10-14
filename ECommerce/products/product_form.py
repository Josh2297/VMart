from django import forms
from django.core.exceptions import ValidationError
from .models import Product
import re
from PIL import Image

# Products Form

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        exclude=["creator"]
        widgets={'product_name':forms.TextInput(attrs={'placeholder':'Enter Product Name'}),'description':forms.TextInput(attrs={'placeholder':'Brief Description of Product'}),\
        'qty':forms.NumberInput(attrs={'placeholder':'Select Quantity'}),'price':forms.NumberInput(attrs={'placeholder':'Enter Price'}),'availability':forms.RadioSelect}
    
    consent=forms.BooleanField(label="Do You Consent To Our Terms and Condition",initial=True)

    def clean_product_name(self):
        value=self.cleaned_data.get("product_name")
        value=value.split(" ");value=' '.join([x.capitalize() for x in value])
        return value

    def clean_description(self):
        value=self.cleaned_data.get("description")
        return value.lower()

    def clean_price(self):
        value=self.cleaned_data.get('price')
        if value<0:
            raise ValidationError("Price Cannot Be Negative")
        return value

    def clean_product_picture(self):
        value=self.cleaned_data.get('product_picture')
        img=Image.open(value)
        if img.size[0]<500:
            raise ValidationError('Picture is of Low Quality and Size. Please Enter a Clearer Picture of Higher Quality')
        return value
    
