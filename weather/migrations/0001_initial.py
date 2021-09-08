# Generated by Django 2.2.19 on 2021-09-07 20:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField(validators=[django.core.validators.MinValueValidator(19.0), django.core.validators.MaxValueValidator(28.0)])),
                ('humidity', models.FloatField(validators=[django.core.validators.MinValueValidator(35.0), django.core.validators.MaxValueValidator(65.0)])),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]