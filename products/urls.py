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
                    AllProductListView,
                    ProductCreateView,
                    ProductUpdateView,
                    ProductDeleteVIew,
                    ProductByCategoryListView,
                    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #Marcas
    path('marcas/', BrandListView.as_view(), name='brands_list'),
    path('marcas/crear/', CreateBrandView.as_view(), name='brand_create'),
    path('marcas/editar/<slug:slug>/', BrandUpdateView.as_view(), name='brand_update'),
    path('marcas/eliminar/<slug:slug>/', BrandDeleteVIew.as_view(), name='brand_delete'),
    #categorias
    path('categorias/', CategoryListView.as_view(), name='categories_list'),
    path('categorias/crear/', CreateCategoryView.as_view(), name='category_create'),
    path('categorias/editar/<slug:slug>/', CategoryUpdateView.as_view(), name='category_update'),
    path('categorias/eliminar/<slug:slug>/', CategoryDeleteVIew.as_view(), name='category_delete'),
    path('categoria/<slug:slug>/<int:id>/', ProductByCategoryListView.as_view(), name='products_by_category'),
    #productos
    path('todos-los-productos/', AllProductListView.as_view(), name='all_products_list'),
    path('productos/crear/', ProductCreateView.as_view(), name='products_create'),
    path('productos/editar/<slug:slug>/', ProductUpdateView.as_view(), name='products_update'),
    path('productos/eliminar/<slug:slug>/', ProductDeleteVIew.as_view(), name='products_delete'),
]
