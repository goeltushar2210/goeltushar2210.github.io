# Generated by Django 2.2.13 on 2020-07-09 17:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_auto_20200709_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('contactus', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='products_men',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='products_women',
            name='timestamp',
        ),
    ]
