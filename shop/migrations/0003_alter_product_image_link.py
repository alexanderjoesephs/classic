# Generated by Django 4.1.6 on 2023-03-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cart_product_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_link',
            field=models.ImageField(upload_to='images/'),
        ),
    ]