# Generated by Django 2.2.13 on 2020-06-28 11:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
