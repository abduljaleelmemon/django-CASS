# Generated by Django 3.0.3 on 2020-03-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0020_auto_20200325_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(),
        ),
    ]
