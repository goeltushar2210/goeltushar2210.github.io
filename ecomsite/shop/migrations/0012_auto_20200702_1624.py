# Generated by Django 2.2.13 on 2020-07-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200702_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='front',
            name='card_image',
            field=models.ImageField(upload_to='men'),
        ),
    ]