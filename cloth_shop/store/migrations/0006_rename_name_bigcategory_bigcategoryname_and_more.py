# Generated by Django 4.0.3 on 2022-04-09 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_bigcategory_category_bigcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bigcategory',
            old_name='name',
            new_name='bigcategoryname',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='categoryname',
        ),
    ]
