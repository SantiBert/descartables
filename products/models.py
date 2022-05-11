from tabnanny import verbose
from django.utils import timezone
from django.db import models

from autoslug import AutoSlugField

capitalizeFirstChar = lambda s: s[:1].upper() + s[1:]

CHOICES = (
	("1", "Disponible"),
	("2", "No disponible")
)

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,verbose_name = "nombre", unique=True)
    slug = AutoSlugField(populate_from='name')
    status = models.CharField(max_length=10, choices=CHOICES)
    created_date = models.DateTimeField(default=timezone.now, verbose_name = "fecha de creación")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, verbose_name = "nombre")
    slug = AutoSlugField(populate_from='name')
    status = models.CharField(max_length=10, choices=CHOICES)
    created_date = models.DateTimeField(default=timezone.now,verbose_name = "fecha de creación")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
    
    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,verbose_name = "marca",null=True, blank=True)
    tag = models.ManyToManyField(Tag, verbose_name = "Tag")
    name = models.CharField(max_length=255, verbose_name = "nombre")
    slug = AutoSlugField(populate_from='name')
    price = models.FloatField(max_length=100,verbose_name = "precio")
    code = models.CharField(max_length=10, unique=True, null=True, blank=True,verbose_name = "código")
    #image = models.ImageField(upload_to="media/product/images/")
    quantity = models.IntegerField(default=0, verbose_name = "cantidad")
    description = models.TextField(null=True, blank=True, verbose_name = "descripción")
    taxs = models.FloatField(max_length=100, default=0, null=True, blank=True, verbose_name="IVA")
    status = models.CharField(max_length=10, choices=CHOICES)
    created_date = models.DateTimeField(default=timezone.now, verbose_name = "fecha de creación")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
    
    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    sub_total = models.FloatField(max_length=100)
    vat = models.FloatField(max_length=100)
    total_amount = models.FloatField(max_length=100)
    discount = models.FloatField(max_length=100)
    grand_total = models.FloatField(max_length=100)
    paid = models.FloatField(max_length=100)
    due = models.FloatField(max_length=100)
    payment_type = models.CharField(max_length=100)
    payment_status = models.IntegerField()
    status = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    rate = models.FloatField(max_length=100)
    total = models.FloatField(max_length=100)
    status = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)