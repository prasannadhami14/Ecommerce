# Generated by Django 5.1.3 on 2025-01-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', null=True, unique=True),
        ),
    ]