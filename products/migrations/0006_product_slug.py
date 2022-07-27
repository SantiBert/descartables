# Generated by Django 4.0.3 on 2022-07-23 23:37

import autoslug.fields
import datetime
from django.db import migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=datetime.datetime(2022, 7, 23, 23, 37, 11, 611471, tzinfo=utc), editable=False, populate_from='name'),
            preserve_default=False,
        ),
    ]