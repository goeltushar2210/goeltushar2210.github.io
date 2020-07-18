# Generated by Django 2.2.13 on 2020-07-10 07:06

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0046_auto_20200710_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='name',
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='namec',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='about',
            name='aboutus',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contactus',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]