# Generated by Django 4.2.6 on 2023-11-22 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_prdbrand_product_prdcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='PRDBrand',
        ),
    ]
