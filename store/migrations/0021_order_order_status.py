# Generated by Django 4.1.2 on 2022-12-11 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_rename_lecategory_subcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='store.orderstatus'),
            preserve_default=False,
        ),
    ]