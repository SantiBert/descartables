from django import forms
from .models import Category, Brand, Subcategory

class BrandForm(forms.ModelForm):
     class Meta:
        model = Brand
        fields = ['name', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
        }
        labels = {
            'name': 'Nombre', 'status': 'Status'
        }
        
class BrandDeleteForm(forms.ModelForm):
     class Meta:
        model = Brand
        fields = ['is_active']

class CategoryForm(forms.ModelForm):
     class Meta:
        model = Category
        fields = ['name', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
        }
        labels = {
            'name': 'Nombre', 'status': 'Status'
        }
        
class CategoryDeleteForm(forms.ModelForm):
     class Meta:
        model = Category
        fields = ['is_active']
        

class SubCategoryForm(forms.ModelForm):
     class Meta:
        model = Subcategory
        fields = ['name', 'status', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
        }
        labels = {
            'name': 'Nombre', 'status': 'Status', 'category':'Categoría'
        }
        
class SubCategoryDeleteForm(forms.ModelForm):
     class Meta:
        model = Subcategory
        fields = ['is_active']