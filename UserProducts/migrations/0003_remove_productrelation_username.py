# Generated by Django 4.2.1 on 2023-11-13 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProducts', '0002_productrelation_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrelation',
            name='userName',
        ),
    ]