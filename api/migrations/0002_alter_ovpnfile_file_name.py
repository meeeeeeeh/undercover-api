# Generated by Django 4.1.2 on 2022-10-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ovpnfile',
            name='file_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]