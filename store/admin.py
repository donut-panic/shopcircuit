from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Product, Order, UnitOrder, Category, ShippingMethod, PaymentMethod, OrderStatus, \
    Subcategory, WishlistItem


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    ordering = ["name"]
    list_display = ["id", "name"]
    list_per_page = 20
    search_fields = ["name"]
    search_help_text = "Enter a category name"


@admin.register(Subcategory)
class SubcategoryAdmin(ModelAdmin):
    ordering = ["name"]
    list_display = ["id", "category_id", "name"]
    list_per_page = 20
    list_filter = ["category_id"]
    search_help_text = "Enter a subcategory name"


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    ordering = ["name"]
    list_display = ["id", "name", "category", "subcategory", "image", "price", "quantity", "tax"]
    list_per_page = 20
    search_fields = ["name"]
    list_filter = ["category"]
    search_help_text = "Enter a product name"


@admin.register(ShippingMethod)
class ShippingMethodAdmin(ModelAdmin):
    ordering = ["shipping_company"]
    list_display = ["id", "service_name", "shipping_company", "price", "tax"]
    list_per_page = 20
    search_fields = ["service_name"]
    list_filter = ["shipping_company"]
    search_help_text = "Enter a service name"


@admin.register(PaymentMethod)
class PaymentMethodAdmin(ModelAdmin):
    ordering = ["service_name"]
    list_display = ["id", "service_name"]
    list_per_page = 20
    search_fields = ["service_name"]
    search_help_text = "Enter a service name"


@admin.register(OrderStatus)
class OrderStatusAdmin(ModelAdmin):
    ordering = ["name"]
    list_display = ["id", "name"]
    list_per_page = 20


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    ordering = ["created"]
    list_display = ["order_by", "order_status", "created", "address_street", "address_postal_code", "address_city", "shipping", "payment_method"]
    list_per_page = 20
    list_filter = ["order_status", "payment_method"]


@admin.register(UnitOrder)
class UnitOrderAdmin(ModelAdmin):
    ordering = ["order_id"]
    list_display = ["order_id", "product_id", "quantity", "price"]
    list_per_page = 20
    list_filter = ["product_id"]


@admin.register(WishlistItem)
class WishlistItemAdmin(ModelAdmin):
    ordering = ["user"]
    list_display = ["user", "product"]
    list_per_page = 20
    list_filter = ["user", "product"]
