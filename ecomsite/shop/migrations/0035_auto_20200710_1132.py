# Generated by Django 2.2.13 on 2020-07-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_auto_20200710_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='new', max_length=50),
        ),
    ]