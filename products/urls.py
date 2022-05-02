from django.contrib import admin
from django.urls import path
from .views import (IndexView, 
                    BrandListView,
                    CreateBrandView,
                    BrandUpdateView,
                    BrandDeleteVIew,
                    CategoryListView, 
                    CreateCategoryView,
                    CategoryUpdateView,
                    CategoryDeleteVIew,
                    SubcategoryListView,
                    CreateSubcategoryView,
                    SubcategoryUpdateView,
                    SubcategoryDeleteVIew,
                    AllProductListView
                    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #Marcas
    path('marcas/', BrandListView.as_view(), name='brands_list'),
    path('marcas/crear', CreateBrandView.as_view(), name='brand_create'),
    path('marcas/editar/<slug:slug>/', BrandUpdateView.as_view(), name='brand_update'),
    path('marcas/eliminar/<slug:slug>/', BrandDeleteVIew.as_view(), name='brand_delete'),
    #categorias
    path('categorias/', CategoryListView.as_view(), name='categories_list'),
    path('categorias/crear', CreateCategoryView.as_view(), name='category_create'),
    path('categorias/editar/<slug:slug>/', CategoryUpdateView.as_view(), name='category_update'),
    path('categorias/eliminar/<slug:slug>/', CategoryDeleteVIew.as_view(), name='category_delete'),
    #subcategorias
    path('subcategorias/', SubcategoryListView.as_view(), name='subcategories_list'),
    path('subcategorias/crear', CreateSubcategoryView.as_view(), name='subcategory_create'),
    path('subcategorias/editar/<slug:slug>/', SubcategoryUpdateView.as_view(), name='subcategory_update'),
    path('subcategorias/eliminar/<slug:slug>/', SubcategoryDeleteVIew.as_view(), name='subcategory_delete'),
    #productos
    path('todos-los-productos/', AllProductListView.as_view(), name='all_products_list'),
]
