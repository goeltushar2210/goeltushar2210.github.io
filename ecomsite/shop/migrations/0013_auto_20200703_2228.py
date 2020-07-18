# Generated by Django 2.2.13 on 2020-07-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20200702_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fronts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(max_length=20)),
                ('card_text', models.CharField(max_length=100)),
                ('card_image', models.ImageField(upload_to='front')),
            ],
        ),
        migrations.DeleteModel(
            name='front',
        ),
    ]