# Generated by Django 3.2 on 2022-11-05 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20221105_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
