# Generated by Django 2.2.13 on 2020-07-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_auto_20200716_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.FloatField(default=0.0, max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0, max_length=50),
        ),
    ]