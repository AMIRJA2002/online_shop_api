# Generated by Django 4.1.1 on 2022-10-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_basketline_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketline',
            name='price',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
