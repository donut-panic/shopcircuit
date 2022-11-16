from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, TextField, ForeignKey, DO_NOTHING, ImageField, DecimalField, IntegerField, \
    DateTimeField


# Create your models here.
class Category(models.Model):
    parent_id = ForeignKey('self', on_delete=DO_NOTHING, blank=True, null=True)
    name = CharField(max_length=512, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = CharField(max_length=512, null=False)
    description = TextField(default='Podaj opis.')
    category = ForeignKey(Category, on_delete=DO_NOTHING)
    image = ImageField(upload_to='static/images', blank=True, null=True)
    price = DecimalField(max_digits=12, decimal_places=2, null=False)
    quantity = IntegerField(null=False)
    tax = DecimalField(max_digits=12, decimal_places=2, null=False)

    def __str__(self):
        return self.name


class ShippingMethod(models.Model):
    shipping_company = CharField(max_length=512, null=False)
    service_name = CharField(max_length=512, null=False)
    price = DecimalField(max_digits=12, decimal_places=2, null=False)
    tax = DecimalField(max_digits=12, decimal_places=2, null=False)

    def __str__(self):
        return self.service_name


class PaymentMethod(models.Model):
    service_name = CharField(max_length=512, null=False)

    def __str__(self):
        return self.service_name


class OrderStatus(models.Model):
    name = CharField(max_length=512)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_by = ForeignKey(User, on_delete=DO_NOTHING)
    ForeignKey(OrderStatus, on_delete=DO_NOTHING)
    created = DateTimeField(default=datetime.now)
    address_street = CharField(max_length=256)
    address_postal_code = CharField(max_length=18)
    address_city = CharField(max_length=128)
    shipping = ForeignKey(ShippingMethod, on_delete=DO_NOTHING)
    payment = DecimalField(max_digits=12, decimal_places=2, null=False)
    payment_method = ForeignKey(PaymentMethod, on_delete=DO_NOTHING)

    def __str__(self):
        return self.id


class UnitOrder(models.Model):
    order_id = ForeignKey(Order, on_delete=DO_NOTHING)
    product_id = ForeignKey(Product, on_delete=DO_NOTHING)
    quantity = IntegerField(null=False)

    def __str__(self):
        return self.id
