# Generated by Django 4.0.4 on 2022-05-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_product_quantity_product_size_delete_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(default='Standart', max_length=10, null=True),
        ),
    ]