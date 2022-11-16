from django.contrib import admin

from store.models import Product, Order, UnitOrder, Category, ShippingMethod, PaymentMethod, OrderStatus

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ShippingMethod)
admin.site.register(PaymentMethod)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(UnitOrder)
















