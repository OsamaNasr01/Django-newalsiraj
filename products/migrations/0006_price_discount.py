# Generated by Django 4.2.3 on 2023-08-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_price_created_at_product_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='discount',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
