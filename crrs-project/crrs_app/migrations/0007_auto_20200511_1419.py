# Generated by Django 2.2.12 on 2020-05-11 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crrs_app', '0006_remove_amg1formdb_unique_identifier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amg1formdb',
            old_name='messages',
            new_name='feedback',
        ),
    ]