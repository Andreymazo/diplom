# Generated by Django 3.2.10 on 2023-05-05 03:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0008_remove_product_price_value_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_value_total', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price.product')),
            ],
            options={
                'verbose_name': 'products',
                'verbose_name_plural': 'products',
                'permissions': [('add_Product', 'Can add Product')],
            },
        ),
    ]
