# Generated by Django 2.2.12 on 2020-05-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crrs_app', '0004_amg1formdb_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='amg1formdb',
            name='unique_identifier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]