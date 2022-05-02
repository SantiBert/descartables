from itertools import product
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import TemplateView,View, CreateView, UpdateView, UpdateView, FormView
from .models import Brand, Category, Subcategory, Product
from .forms import CategoryForm, CategoryDeleteForm, BrandForm, BrandDeleteForm, SubCategoryForm, SubCategoryDeleteForm

class IndexView(TemplateView):
    template_name = 'index.html'
    
#Vistas de Marcas
class BrandListView(View):
    def get(self, request, *args, **kwargs):
        try:
            brands = Brand.objects.filter(is_active=True)
        except:
            brands = None

        context = {
            "brands": brands,
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
            for i in range(len(categories)):
                subcatory = list(Subcategory.objects.filter(category=i).values())
                categories[i].subcatories = subcatory
        except:
            categories = None

        context = {
            "categories": categories,
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
        except:
            subcategories = None

        context = {
            "subcategories": subcategories,
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
        except:
            products = None

        context = {
            "products": products,
        }
        return render(request, 'products.html', context)

class ProductByCategoryListView(View):
    def get(self, request,id, *args, **kwargs):
        try:
            category = Category.objects.get(id=id)
            products = Product.objects.filter(is_active=True, category = category)
        except:
            products = None

        context = {
            "products": products,
        }
        return render(request, 'products.html', context)