# Generated by Django 4.2 on 2023-05-08 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_remove_order_total_amount_remove_order_total_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
