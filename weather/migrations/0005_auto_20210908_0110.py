# Generated by Django 2.2.19 on 2021-09-07 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_auto_20210908_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='date',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='time',
        ),
    ]
