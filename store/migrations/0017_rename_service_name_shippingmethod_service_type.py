# Generated by Django 4.1.2 on 2022-11-29 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_rename_shipping_company_shippingmethod_shipping_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingmethod',
            old_name='service_name',
            new_name='service_type',
        ),
    ]
