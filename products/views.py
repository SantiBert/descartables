
from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import TemplateView,View, CreateView, UpdateView, UpdateView, FormView

from .models import Brand, Category, Subcategory, Product
from .forms import (CategoryForm, 
                    CategoryDeleteForm, 
                    BrandForm, 
                    BrandDeleteForm, 
                    SubCategoryForm, 
                    SubCategoryDeleteForm, 
                    ProductForm,
                    ProductDeleteForm)

class IndexView(TemplateView):
    template_name = 'index.html'
    
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

#Vistas de Categorias
class CategoryListView(View):
    def get(self, request, *args, **kwargs):
        try:
            categories = Category.objects.filter(is_active=True)
            for categoryline in categories:
                subcatory = list(Subcategory.objects.filter(category=categoryline).values())
                categoryline.subcatories = subcatory                          
            paginator = Paginator(categories, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        except:
            categories = None
            page_obj = None

        context = {
            "categories": categories,
            "page_obj":page_obj
        }
        return render(request, 'categories.html', context)
    
class CreateCategoryView(CreateView):
    model = Category
    template_name = 'forms/category-form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories_list')
    

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'forms/category-update-form.html'
    form_class = CategoryForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('categories_list')
    text_object_name = 'category'

class CategoryDeleteVIew(UpdateView):
    model = Category
    template_name = 'forms/category-delete.html'
    form_class = CategoryDeleteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('categories_list')
    text_object_name = 'category'
    
    
#Vistas de subcategorias
class SubcategoryListView(View):
    def get(self, request, *args, **kwargs):
        try:
            subcategories = Subcategory.objects.filter(is_active=True)
            paginator = Paginator(subcategories, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
        except:
            subcategories = None
            page_obj = None

        context = {
            "subcategories": subcategories,
            "page_obj":page_obj,
        }
        return render(request, 'subcategories.html', context)
    
class CreateSubcategoryView(CreateView):
    model = Subcategory
    template_name = 'forms/subcategory-form.html'
    form_class = SubCategoryForm
    success_url = reverse_lazy('subcategories_list')
    

class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    template_name = 'forms/subcategory-update-form.html'
    form_class = SubCategoryForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('subcategories_list')
    text_object_name = 'subcategory'

class SubcategoryDeleteVIew(UpdateView):
    model = Subcategory
    template_name = 'forms/subcategory-delete.html'
    form_class = SubCategoryDeleteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('subcategories_list')
    text_object_name = 'subcategory'
    
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

class ProductDeleteVIew(UpdateView):
    model = Product
    template_name = 'forms/product-delete.html'
    form_class = ProductDeleteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('all_products_list')
    text_object_name = 'product'

class ProductByCategoryListView(View):
    def get(self, request,id, *args, **kwargs):
        try:
            category = Category.objects.get(id=id)
            products = Product.objects.filter(is_active=True, category = category)
            for productline in products:
                productline.final_price =  productline.price + (productline.price * (productline.taxs /100))
            paginator = Paginator(products, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        except:
            category = None
            products = None
            page_obj = None

        context = {
            "category": category,
            "products": products,
            'page_obj': page_obj,
        }
        return render(request, 'products_by_category.html', context)
    
class ProductBySubcategoryListView(View):
    def get(self, request,id, *args, **kwargs):
        try:
            subcategory = Subcategory.objects.get(id=id)
            products = Product.objects.filter(is_active=True, subcategory = subcategory)
            for productline in products:
                productline.final_price =  productline.price + (productline.price * (productline.taxs /100))
            paginator = Paginator(products, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
        except:
            subcategory = None
            products = None
            page_obj = None

        context = {
            "subcategory": subcategory,
            "products": products,
            'page_obj': page_obj,
        }
        return render(request, 'products_by_subcategory.html', context)