from django.contrib import admin
from .models import Brand, Category, Subcategory, Product

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)