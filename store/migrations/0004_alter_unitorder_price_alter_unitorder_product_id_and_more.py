# Generated by Django 4.1.2 on 2022-11-23 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_unitorder_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitorder',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='unitorder',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.product'),
        ),
        migrations.AlterField(
            model_name='unitorder',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]