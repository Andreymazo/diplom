# Generated by Django 3.2.10 on 2023-05-04 13:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0005_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_value',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_value_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
    ]