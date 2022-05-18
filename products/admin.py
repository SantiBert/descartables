from django.contrib import admin
from .models import Brand, Tag, Product

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ProductResourseces(resources.ModelResource):
    class Meta:
        model = Product


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name','created_date')
    search_fields = ['name']
    resource_class = ProductResourseces
    
    
class BrandResourseces(resources.ModelResource):
    class Meta:
        model = Brand


class BrandAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name','created_date')
    search_fields = ['name']
    resource_class = BrandResourseces

class TagResourseces(resources.ModelResource):
    class Meta:
        model = Tag


class TagAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name','created_date')
    search_fields = ['name']
    resource_class = TagResourseces


admin.site.register(Brand, BrandAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Product, ProductAdmin)