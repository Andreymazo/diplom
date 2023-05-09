from django.contrib import admin

from price.models import Product, CustomUser, Category

admin.site.register(Product)

admin.site.register(CustomUser)

admin.site.register(Category)
