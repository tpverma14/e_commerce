# Generated by Django 2.2 on 2019-05-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_auto_20190524_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='additional_description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=5000),
        ),
    ]
