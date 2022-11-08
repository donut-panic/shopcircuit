from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, TextField, ForeignKey, DO_NOTHING, ImageField, DecimalField, IntegerField, \
    DateTimeField


# Create your models here.



class Product(models.Model):
    name = CharField(max_length=512, null=False)
    description = TextField(default='Podaj opis.')
    category = ForeignKey('Category', on_delete=DO_NOTHING)
    image = ImageField(upload_to='static/images', blank=True, null=True)
    price = DecimalField(max_digits=12, decimal_places=2, null=False)
    quantity = IntegerField(null=False)



class Category(models.Model):
    parent_id = ForeignKey('self', on_delete= DO_NOTHING)
    name = CharField(max_length=512 , null=False)


class Order(models.Model):
    STATUS = [
        ('payment', 'Waiting For Payment'),
        ('pending', 'Your order is being confirmed by us'),
        ('delivery', 'Your order is in delivery'),
        ('done', 'Product delivered'),
    ]
    SHIPPING= [('DHL', 'DHL'),
               ('poczta', 'Pocztex Kurier'),
               ('inpost', 'InPost'),
               ('orlen', 'Orlen Paczka')
    ]
    PAYMENT = [('creditcard', 'Chose credit card'),
               ('blik', 'Pay by BLIK'),
               ('paypal', 'Pay by PayPal'),
               ('banktransfer', 'Make a transfer via your bank')
    ]

    order_by = IntegerField(null= False)
    status = CharField(max_length=128, choices=STATUS, default='payment')
    created = DateTimeField(default=datetime.now)
    address_street = CharField(max_length=256)
    address_postal_code = CharField(max_length=18)
    address_city = CharField(max_length=128)
    shipping = CharField(max_length=128, choices=SHIPPING, default='inpost')
    payment = DecimalField(max_digits=12, decimal_places=2, null=False)
    payment_method = CharField(max_length=128, choices=PAYMENT, default='creditcard')


    # @property
    # def GDP_per_capita(self):
    #     return round(self.GDP / self.Populacja, 3)


class UnitOrder(models.Model):
    order_id = ForeignKey('Order', on_delete=DO_NOTHING)
    product_id = ForeignKey('Product', on_delete=DO_NOTHING)
    quantity = IntegerField(null= False)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password =






