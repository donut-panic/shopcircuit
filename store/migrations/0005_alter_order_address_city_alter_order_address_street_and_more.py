# Generated by Django 4.1.2 on 2022-11-23 13:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_alter_unitorder_price_alter_unitorder_product_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_city',
            field=models.CharField(max_length=128, verbose_name='City name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_street',
            field=models.CharField(max_length=256, verbose_name='Adress Street (please provide full name)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Beginning of purchase'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(default='Podaj opis.'),
        ),
    ]
