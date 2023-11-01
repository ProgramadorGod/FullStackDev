# Generated by Django 4.2.1 on 2023-11-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Price', models.FloatField(max_length=28)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='itemspics')),
            ],
        ),
    ]
