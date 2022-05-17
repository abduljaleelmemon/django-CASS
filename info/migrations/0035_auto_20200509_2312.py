# Generated by Django 3.0.3 on 2020-05-09 18:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0034_auto_20200509_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='fee',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)]),
        ),
        migrations.AlterField(
            model_name='time',
            name='day',
            field=models.CharField(choices=[('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Monday', 'Monday'), ('Wednesday', 'Wednesday'), ('Tuesday', 'Tuesday'), ('Saturday', 'Saturday')], default='Monday', max_length=20),
        ),
    ]
