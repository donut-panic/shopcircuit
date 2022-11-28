from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, TextField, ForeignKey, DO_NOTHING, ImageField, DecimalField, IntegerField, \
    DateTimeField


from smart_selects.db_fields import ChainedForeignKey
from tinymce.models import HTMLField


# Create your models here.
class Category(models.Model):
    name = CharField(max_length=512, null=False, default='other')

    def __str__(self):
        return self.name

class LeCategory(models.Model):
    category_id = ForeignKey(Category, on_delete=DO_NOTHING, default='other')
    name = CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = CharField(max_length=512, null=False)
    description = HTMLField(default='Podaj opis.')
    category = ForeignKey(Category, on_delete=DO_NOTHING)
    subcategory = ChainedForeignKey(
        LeCategory,
        chained_field='category',
        chained_model_field='category_id',
        show_all=False,
        auto_choose=True,
        sort=True
    )
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
    created = DateTimeField(default=datetime.now, verbose_name='Beginning of purchase')
    address_street = CharField(max_length=256, verbose_name='')
    address_postal_code = CharField(max_length=18)
    address_city = CharField(max_length=128, verbose_name='City name')
    shipping = ForeignKey(ShippingMethod, on_delete=DO_NOTHING)
    payment = DecimalField(max_digits=12, decimal_places=2, null=False)
    payment_method = ForeignKey(PaymentMethod, on_delete=DO_NOTHING)

    def __str__(self):
        return f'{self.id}'


class UnitOrder(models.Model):
    order_id = ForeignKey(Order, on_delete=DO_NOTHING)
    product_id = ForeignKey(Product, on_delete=DO_NOTHING)
    quantity = IntegerField(null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return f'{self.id}'
