# Generated by Django 2.2.13 on 2020-07-10 06:08

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0038_auto_20200710_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='aboutus',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contactus',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=1000),
        ),
    ]
