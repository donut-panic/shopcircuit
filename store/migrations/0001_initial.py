import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('payment', 'Waiting For Payment'), ('pending', 'Your order is being confirmed by us'), ('delivery', 'Your order is in delivery'), ('done', 'Product delivered')], default='payment', max_length=128)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('address_street', models.CharField(max_length=256)),
                ('address_postal_code', models.CharField(max_length=18)),
                ('address_city', models.CharField(max_length=128)),
                ('shipping', models.CharField(choices=[('DHL', 'DHL'), ('poczta', 'Pocztex Kurier'), ('inpost', 'InPost'), ('orlen', 'Orlen Paczka')], default='inpost', max_length=128)),
                ('payment', models.DecimalField(decimal_places=2, max_digits=12)),
                ('payment_method', models.CharField(choices=[('creditcard', 'Chose credit card'), ('blik', 'Pay by BLIK'), ('paypal', 'Pay by PayPal'), ('banktransfer', 'Make a transfer via your bank')], default='creditcard', max_length=128)),
                ('order_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField(default='Podaj opis.')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantity', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Category')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='UnitOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.Product')),
            ],
        ),
    ]
