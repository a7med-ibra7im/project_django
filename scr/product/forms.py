from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
          'PRDName', 
          'PRDCategory', 
          'PRDVariant',
          'PRDDesc',
          'PRDImage', 
          'PRDPrice',
          'PRDDiscountprice', 
          'PRDCost',
          'PRDCreated',
          'PRDBrand',
          'PRDSlug',
          ]
    # You can also add custom validation methods if needed
        widgets = {
            'PRDName':forms.TextInput(attrs={'class':'form-control',}) ,
            'PRDCategory':forms.Select(attrs={'class':'form-control'})  ,
            'PRDVariant':forms.Select(attrs={'class':'form-control'})  ,
            'PRDDesc':forms.TextInput(attrs={'class':'form-control'}) ,
            'PRDImage': forms.FileInput(attrs={'class': 'form-control','required':False}),
            'PRDPrice': forms.NumberInput(attrs={'class':'form-control'}), 
            'PRDDiscountprice':forms.NumberInput(attrs={'class':'form-control','required':False}), 
            'PRDCost':forms.NumberInput(attrs={'class':'form-control','required':False}),
            'PRDCreated': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}) ,
            'PRDBrand':forms.Select(attrs={'class': 'form-control'}),
            'PRDSlug':forms.TextInput(attrs={'class':'form-control'}) ,
          }
  
