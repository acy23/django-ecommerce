# Generated by Django 4.0.3 on 2022-04-09 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_name_bigcategory_bigcategoryname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bigcategory',
            old_name='bigcategoryname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='categoryname',
            new_name='name',
        ),
    ]