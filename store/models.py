from datetime import datetime
import json

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, TextField, ForeignKey, DO_NOTHING, ImageField, DecimalField, IntegerField, \
    DateTimeField, CASCADE

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

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class ShippingMethod(models.Model):
    shipping_name = CharField(max_length=512, null=False)
    service_type = CharField(max_length=512, null=False)
    price = DecimalField(max_digits=12, decimal_places=2, null=False)
    tax = DecimalField(max_digits=12, decimal_places=2, null=False)

    def __str__(self):
        return self.shipping_name

    @property
    def price_with_tax(self):
        return float(self.price) + float(self.price) * float(self.tax)


class PaymentMethod(models.Model):
    service_name = CharField(max_length=512, null=False)

    def __str__(self):
        return self.service_name


class OrderStatus(models.Model):
    name = CharField(max_length=512)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_by = ForeignKey(User, on_delete=DO_NOTHING, verbose_name='Ordered by')
    ForeignKey(OrderStatus, on_delete=DO_NOTHING)
    created = DateTimeField(default=datetime.now, verbose_name='Beginning of purchase')
    address_street = CharField(max_length=256, verbose_name='')
    address_postal_code = CharField(max_length=18)
    address_city = CharField(max_length=128, verbose_name='City name')
    shipping = ForeignKey(ShippingMethod, on_delete=DO_NOTHING)
    payment_method = ForeignKey(PaymentMethod, on_delete=DO_NOTHING, default=1)

    def __str__(self):
        return f'{self.id}'


class UnitOrder(models.Model):
    order_id = ForeignKey(Order, on_delete=CASCADE)
    product_id = ForeignKey(Product, on_delete=CASCADE)
    quantity = IntegerField(null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return f'{self.id}'


class Wishlist(models.Model):
    user = ForeignKey(User, on_delete=DO_NOTHING)
    products = CharField(max_length=2048, null=False, default="{}")

    def set_products(self, products):
        self.products = json.dumps(products)

    def get_products(self):
        return json.loads(self.products)

    def __str__(self):
        return f"Wishlist #{self.id}"