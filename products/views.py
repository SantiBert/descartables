import pandas as pd

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic import TemplateView,View, CreateView, UpdateView, UpdateView, FormView
from django.db.models import Q

from .models import Brand, Tag, Product
from .forms import (TagForm, 
                    TagDeleteForm, 
                    BrandForm, 
                    BrandDeleteForm, 
                    ProductForm,
                    ProductDeleteForm,
                    UploadFileForm,
                    ChagePriceByTagForm)


class IndexView(TemplateView):
    template_name = 'dashboard.html'
    
class ChangePriceByTagView(FormView):
    form_class = ChagePriceByTagForm
    template_name = 'upgradates/change_price_by_tags.html'
    success_url = reverse_lazy('index')
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            prince = form.cleaned_data.get('price')
            tags = form.cleaned_data.get('tags')
            print(prince, tags)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    
class ChangeIVAByTagView(View):
    def get(self, request, *args, **kwargs):
        try:
            tags = Tag.objects.filter(is_active=True)
        except:
            tags = None

        context = {
            "tags": tags
        }
        return render(request,'upgradates/change_iva_by_tags.html', context)

class ChangePriceByBrandView(View):
    def get(self, request, *args, **kwargs):
        try:
            brands = Brand.objects.filter(is_active=True)
        except:
            brands = None

        context = {
            "brands": brands
        }
        return render(request,'upgradates/change_price_by_brand.html', context)

class ChangeIVAByBrandView(View):
    def get(self, request, *args, **kwargs):
        try:
            brands = Brand.objects.filter(is_active=True)
        except:
            brands = None

        context = {
            "brands": brands
        }
        return render(request,'upgradates/change_iva_by_brands.html', context)

#Vistas de Marcas

class BrandListView(View):
    def get(self, request, *args, **kwargs):
        try:
            brands = Brand.objects.filter(is_active=True)
            paginator = Paginator(brands, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        except:
            brands = None
            page_obj = None

        context = {
            "brands": brands,
            "page_obj": page_obj
        }
        return render(request, 'brands.html', context)
    

class CreateBrandView(CreateView):
    model = Brand
    template_name = 'forms/brand-form.html'
    form_class = BrandForm
    success_url = reverse_lazy('brands_list')
    

class BrandUpdateView(UpdateView):
    model = Brand
    template_name = 'forms/brand-update-form.html'
    form_class = BrandForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('brands_list')
    text_object_name = 'brand'


class BrandDeleteVIew(UpdateView):
    model = Brand
    template_name = 'forms/brand-delete.html'
    form_class = BrandDeleteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('brands_list')
    text_object_name = 'brand'


#Vistas de Tags

class TagListView(View):
    def get(self, request, *args, **kwargs):
        try:
            tags = Tag.objects.filter(is_active=True)
            paginator = Paginator(tags, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        except:
            tags = None
            page_obj = None

        context = {
            "tags": tags,
            "page_obj":page_obj
        }
        return render(request, 'tags.html', context)
    

class CreateTagView(CreateView):
    model = Tag
    template_name = 'forms/tag-form.html'
    form_class = TagForm
    success_url = reverse_lazy('tags_list')
    

class TagUpdateView(UpdateView):
    model = Tag
    template_name = 'forms/tag-update-form.html'
    form_class = TagForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('tags_list')
    text_object_name = 'tag'


class TagDeleteVIew(UpdateView):
    model = Tag
    template_name = 'forms/tag-delete.html'
    form_class = TagDeleteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('tags_list')
    text_object_name = 'tag'


#Vistas de productos

class AllProductListView(View):
    def get(self, request, *args, **kwargs):
        try:
            products = Product.objects.filter(is_active=True)
            for productline in products:
                productline.final_price =  productline.price + (productline.price * (productline.taxs /100))
            paginator = Paginator(products, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        except:
            products = None
            page_obj = None

        context = {
            "products": products,
            'page_obj': page_obj,
        }
        return render(request, 'products.html', context)

    def post(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar") 
        if queryset: 
            products = Product.objects.filter( 
                Q(name__icontains=queryset) | 
                Q(tag__name__icontains=queryset, tag__status="1", tag__is_active=True),                
                status="1",
                is_active=True 
            ).distinct()
        else:
            return self.get(request)
        context = { 
            "products": products, 
        } 
        return render(request, 'products.html', context)
    

class ProductCreateView(CreateView):
    model = Product
    template_name = 'forms/product-form.html'
    form_class = ProductForm
    success_url = reverse_lazy('all_products_list')
    

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'forms/product-update-form.html'
    form_class = ProductForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('all_products_list')
    text_object_name = 'product'


class ProductDeleteView(UpdateView):
    model = Product
    template_name = 'forms/product-delete.html'
    form_class = ProductDeleteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('all_products_list')
    text_object_name = 'product'


class ProductByTagListView(View):
    def get(self, request, id, *args, **kwargs):
        try:
            tag = Tag.objects.get(id=id)
            products = Product.objects.filter(is_active=True, tag = tag)
            for productline in products:
                productline.final_price =  productline.price + (productline.price * (productline.taxs /100))
            paginator = Paginator(products, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        except:
            tag = None
            products = None
            page_obj = None

        context = {
            "tag": tag,
            "products": products,
            'page_obj': page_obj,
        }
        return render(request, 'products_by_tag.html', context)
"""    
class UploadFileView(View):
    template_name = "upload.html"
    form_class = UploadFileForm
    success_url = reverse_lazy('all_products_list')
    
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        file = request.FILES('file_field')
        if form.is_valid():
            data = pd.read_csv(file, header=0, encoding="UTF-8")
            print(data)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
"""

class UploadFileView(FormView):
    
    template_name = 'upload.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('all_products_list')
    
    def post(self,request, *args, **kwarg):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES['file']
                data = pd.read_csv(file, header=0, encoding="UTF-8")
                print(data)
        else:
            form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})
        
 