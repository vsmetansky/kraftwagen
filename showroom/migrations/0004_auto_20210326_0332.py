# Generated by Django 3.1.7 on 2021-03-26 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0003_auto_20210326_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='facility',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
