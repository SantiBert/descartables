from django import forms
from .models import Category, Brand, Subcategory, Product

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
        
class ProductForm(forms.ModelForm):
     class Meta:
        model = Product
        fields = [ 'name', 'brand','category', 'subcategory', 'price' , 'code' ,'quantity' , 'description' ,'taxs', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Codígo'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
            'taxs': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Impuestos'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'status': forms.Select()
        }
        labels = {
            'name': 'Nombre', 'status': 'Status', 'category':'Categoría', 'subcategory':'Subcategoría', 'price':'Precio' , 'code':'Codígo' ,'quantity':'Cantidad' , 'description':'Descripción' ,'taxs':'Inpuestos', 'status':'Status'
        }
        
class ProductDeleteForm(forms.ModelForm):
     class Meta:
        model = Product
        fields = ['is_active']