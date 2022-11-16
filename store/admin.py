from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Product, Order, UnitOrder, TypeProduct, SubTypeProduct

admin.site.register(TypeProduct)

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(UnitOrder)



@admin.register(SubTypeProduct)
class ProfileAdmin(ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'type_product', 'sub_type']
    # list_display_links = ['id', 'name']
    # list_per_page = 20





