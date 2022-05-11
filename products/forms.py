from django import forms
from .models import Tag, Brand, Product

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

class TagForm(forms.ModelForm):
     class Meta:
        model = Tag
        fields = ['name', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status':  forms.Select(attrs={'class': 'form-control', 'id':'exampleFormControlSelect1'})
        }
        
class TagDeleteForm(forms.ModelForm):
     class Meta:
        model = Tag
        fields = ['is_active']
        

        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'name', 'brand','tag', 'price' , 'code' ,'quantity' , 'description' ,'taxs', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'code': forms.TextInput(attrs={'class': 'form-control',}),
            'price': forms.NumberInput(attrs={'class': 'form-control', }),
            'quantity': forms.NumberInput(attrs={'class': 'form-control',}),
            'taxs': forms.NumberInput(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control',}),
            'brand':  forms.Select(attrs={'class': 'form-control', 'id':'exampleFormControlSelect1'}),
            'tag':  forms.SelectMultiple(attrs={'class': 'form-control', 'id':'exampleFormControlSelect1'}),
            'status': forms.Select(attrs={'class': 'form-control', 'id':'exampleFormControlSelect1'})
        }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tag'].queryset = Tag.objects.filter(status=1, is_active=1)
        self.fields['brand'].queryset = Brand.objects.filter(status=1, is_active=1)
        """
        labels = {
            'name': 'Nombre', 'status': 'Status', 'tag':'Tag', 'price':'Precio' , 'code':'Codígo' ,'quantity':'Cantidad' , 'description':'Descripción' ,'taxs':'Inpuestos', 'status':'Status'
        }
        """
        
class ProductDeleteForm(forms.ModelForm):
     class Meta:
        model = Product
        fields = ['is_active']