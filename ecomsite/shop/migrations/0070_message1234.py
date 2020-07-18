# Generated by Django 2.2.13 on 2020-07-12 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0069_delete_message1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message1234',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default=True, max_length=100)),
                ('ip', models.CharField(blank=True, max_length=50)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]