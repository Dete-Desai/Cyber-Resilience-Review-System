# Generated by Django 2.2.12 on 2020-06-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crrs_app', '0017_auto_20200627_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amg1formdb',
            name='amg1_complete',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='amg1formdb',
            name='amg1_incomplete',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1, null=True),
        ),
    ]