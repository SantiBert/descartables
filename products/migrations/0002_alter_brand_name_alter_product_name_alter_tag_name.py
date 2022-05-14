# Generated by Django 4.0.3 on 2022-05-13 19:56

from django.db import migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=products.models.NameField(max_length=255, unique=True, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=products.models.NameField(max_length=255, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=products.models.NameField(max_length=255, unique=True, verbose_name='nombre'),
        ),
    ]
