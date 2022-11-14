from django.contrib import admin

from djangorestapp.models import Product, Todo

# Register your models here.

admin.site.register(Todo)
admin.site.register(Product)