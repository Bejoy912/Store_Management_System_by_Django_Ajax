# Generated by Django 3.2.12 on 2022-07-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0008_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ids',
            field=models.IntegerField(default=100),
        ),
    ]
