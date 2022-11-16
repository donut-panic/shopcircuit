from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Product, Order, UnitOrder, TypeProduct, SubTypeProduct

admin.site.register(TypeProduct)

admin.site.register(Order)
admin.site.register(UnitOrder)















