# Generated by Django 3.2.4 on 2021-06-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]