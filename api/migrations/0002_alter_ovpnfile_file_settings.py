# Generated by Django 4.1.2 on 2022-10-22 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovpnfile',
            name='file_settings',
            field=models.TextField(max_length=10000),
        ),
    ]