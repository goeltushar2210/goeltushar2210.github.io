# Generated by Django 2.2.13 on 2020-07-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200710_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=50),
        ),
    ]