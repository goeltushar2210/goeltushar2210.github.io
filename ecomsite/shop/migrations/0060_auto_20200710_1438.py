# Generated by Django 2.2.13 on 2020-07-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0059_auto_20200710_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='abouta',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='contactc',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
