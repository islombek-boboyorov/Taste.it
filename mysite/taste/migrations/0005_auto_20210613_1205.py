# Generated by Django 3.2.4 on 2021-06-13 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taste', '0004_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='author_age',
            new_name='a_age',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='author_description',
            new_name='a_description',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='author_image',
            new_name='a_image',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='author_name',
            new_name='a_name',
        ),
    ]
