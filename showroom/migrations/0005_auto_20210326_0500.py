# Generated by Django 3.1.7 on 2021-03-26 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0004_auto_20210326_0332'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Order',
        ),
    ]