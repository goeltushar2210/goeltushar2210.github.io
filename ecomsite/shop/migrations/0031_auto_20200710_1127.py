# Generated by Django 2.2.13 on 2020-07-10 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_auto_20200710_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='name',
            new_name='title',
        ),
    ]
