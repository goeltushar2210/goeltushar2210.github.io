# Generated by Django 2.2.13 on 2020-07-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200702_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='front',
            name='card_image',
            field=models.ImageField(upload_to='front'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='men'),
        ),
    ]
