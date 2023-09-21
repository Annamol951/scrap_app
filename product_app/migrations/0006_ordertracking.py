# Generated by Django 4.2 on 2023-05-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_remove_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_placed_on', models.DateField(auto_now_add=True)),
                ('shipped_on', models.DateField(auto_now_add=True)),
                ('delivered_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
