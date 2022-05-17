# Generated by Django 3.0.3 on 2020-03-05 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20200304_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='dept',
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(default='Mathematics', on_delete=django.db.models.deletion.CASCADE, to='info.Course'),
        ),
    ]
