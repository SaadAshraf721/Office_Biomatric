# Generated by Django 3.0 on 2021-04-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0004_update_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update_product_price',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
