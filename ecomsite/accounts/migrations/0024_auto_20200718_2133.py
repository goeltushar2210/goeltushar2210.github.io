# Generated by Django 2.2.13 on 2020-07-18 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_remove_user_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile1',
            new_name='UserProfile',
        ),
    ]