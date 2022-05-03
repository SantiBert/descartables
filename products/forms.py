from django import forms
from .models import Category, Brand, Subcategory, Product

class BrandForm(forms.ModelForm):
     class Meta:
        model = Brand
        fields = ['name', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status':  forms.Select(attrs={'class': 'form-control', 'id':'exampleFormControlSelect1'})
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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status':  forms.Select(attrs={'class': 'form-control', 'id':'exampleFormControlSelect1'})
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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status':  forms.Select(attrs={'class': 'form-control', 'id':'exampleFormControlSelect1'}),
            'category':  forms.Select(attrs={'class': 'form-control', 'id':'exampleFormControlSelect1'})
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
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'code': forms.TextInput(attrs={'class': 'form-control',}),
            'price': forms.NumberInput(attrs={'class': 'form-control', }),
            'quantity': forms.NumberInput(attrs={'class': 'form-control',}),
            'taxs': forms.NumberInput(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control',}),
            'category':  forms.Select(attrs={'class': 'form-control', 'id':'exampleFormControlSelect1'}),
            'subcategory':  forms.Select(attrs={'class': 'form-control', 'id':'exampleFormControlSelect1'}),
            'status': forms.Select(attrs={'class': 'form-control', 'id':'exampleFormControlSelect1'})
        }
        """
        labels = {
            'name': 'Nombre', 'status': 'Status', 'category':'Categoría', 'subcategory':'Subcategoría', 'price':'Precio' , 'code':'Codígo' ,'quantity':'Cantidad' , 'description':'Descripción' ,'taxs':'Inpuestos', 'status':'Status'
        }
        """
        
class ProductDeleteForm(forms.ModelForm):
     class Meta:
        model = Product
        fields = ['is_active']