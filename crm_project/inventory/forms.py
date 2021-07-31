from django import forms
from . import models


class CompanyProductForm(forms.ModelForm):

    class Meta:
        model = models.CompanyProduct
        fields = [
            'name',
            'has_taxation',
            'image_catalog',
            'pdf_catalog',
            'price',
            'technical_features',
            'related_with_manufacturedـproducts',
        ]
