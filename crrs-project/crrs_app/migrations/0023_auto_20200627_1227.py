# Generated by Django 2.2.12 on 2020-06-27 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crrs_app', '0022_auto_20200627_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amg1formdb',
            name='amg1_complete',
        ),
        migrations.RemoveField(
            model_name='amg1formdb',
            name='amg1_incomplete',
        ),
    ]