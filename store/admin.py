from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Product, Order, UnitOrder, Category, ShippingMethod, PaymentMethod, OrderStatus, \
    Subcategory, WishlistItem

admin.site.register(ShippingMethod)
admin.site.register(PaymentMethod)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(UnitOrder)
admin.site.register(WishlistItem)


@admin.register(Subcategory)
class SubcategoryAdmin(ModelAdmin):
    ordering = ["category_id"]
    list_display = ["id", "category_id", "name"]
    list_per_page = 20
    list_filter = ["category_id"]
    search_help_text = "Wprowadź nazwę interesującgo Ciebie urządzenia"


@admin.register(Category)
class ProfileAdmin(ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "name"]
    list_per_page = 20
    search_fields = ["name"]
    search_help_text = "Wprowadź nazwę interesującgo Ciebie urządzenia"


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    ordering = ["id"]
    list_display = ["id", "name", "category", "subcategory", "price"]
    list_per_page = 20
    search_fields = ["name"]
    search_help_text = "Wprowadź nazwę interesującgo Ciebie urządzenia"
