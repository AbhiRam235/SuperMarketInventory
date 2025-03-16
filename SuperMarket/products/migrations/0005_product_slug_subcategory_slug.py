# Generated by Django 5.1.7 on 2025-03-15 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
