# Generated by Django 3.0 on 2020-01-13 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200112_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='default',
            new_name='default_address',
        ),
    ]