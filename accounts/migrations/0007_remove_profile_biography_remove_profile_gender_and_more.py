# Generated by Django 4.1.2 on 2022-12-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='house',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='postal_code',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='street',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
