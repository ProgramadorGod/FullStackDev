# Generated by Django 4.2.1 on 2023-12-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_userproducts_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproducts',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
