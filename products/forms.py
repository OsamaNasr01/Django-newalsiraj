
from django import forms
from .models import Category, Product, Brand




class AddCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'brand')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['brand'].widget.attrs.update({'class': 'form-control'})


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ('name', 'country', 'description', 'category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['country'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
