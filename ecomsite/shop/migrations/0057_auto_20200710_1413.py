# Generated by Django 2.2.13 on 2020-07-10 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0056_about_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='About',
            new_name='Aboutus',
        ),
        migrations.RenameModel(
            old_name='Contact',
            new_name='Contactus',
        ),
    ]
