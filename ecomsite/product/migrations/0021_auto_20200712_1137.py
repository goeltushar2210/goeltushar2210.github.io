# Generated by Django 2.2.13 on 2020-07-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20200710_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('T', 'T'), ('F', 'F')], max_length=20),
        ),
    ]
