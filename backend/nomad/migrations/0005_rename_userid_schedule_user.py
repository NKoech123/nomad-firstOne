# Generated by Django 4.1.3 on 2022-11-07 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomad', '0004_remove_vendor_businesscategoryid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='userId',
            new_name='user',
        ),
    ]