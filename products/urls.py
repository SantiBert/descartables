from django.contrib import admin
from django.urls import path
from .views import (IndexView, 
                    BrandListView,
                    CreateBrandView,
                    BrandUpdateView,
                    BrandDeleteVIew,
                    TagListView, 
                    CreateTagView,
                    TagUpdateView,
                    TagDeleteVIew,
                    AllProductListView,
                    ProductCreateView,
                    ProductUpdateView,
                    ProductDeleteView,
                    ProductByTagListView,
                    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #Marcas
    path('marcas/', BrandListView.as_view(), name='brands_list'),
    path('marcas/crear/', CreateBrandView.as_view(), name='brand_create'),
    path('marcas/editar/<slug:slug>/', BrandUpdateView.as_view(), name='brand_update'),
    path('marcas/eliminar/<slug:slug>/', BrandDeleteVIew.as_view(), name='brand_delete'),
    #tags
    path('tags/', TagListView.as_view(), name='tags_list'),
    path('tags/crear/', CreateTagView.as_view(), name='tag_create'),
    path('tags/editar/<slug:slug>/', TagUpdateView.as_view(), name='tag_update'),
    path('tags/eliminar/<slug:slug>/', TagDeleteVIew.as_view(), name='tag_delete'),
    path('tag/<slug:slug>/<int:id>/', ProductByTagListView.as_view(), name='products_by_tag'),
    #productos
    path('todos-los-productos/', AllProductListView.as_view(), name='all_products_list'),
    path('productos/crear/', ProductCreateView.as_view(), name='products_create'),
    path('productos/editar/<slug:slug>/', ProductUpdateView.as_view(), name='products_update'),
    path('productos/eliminar/<slug:slug>/', ProductDeleteView.as_view(), name='products_delete'),
]
