# Generated by Django 3.1.2 on 2021-12-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20211206_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customvariable',
            name='variable',
        ),
        migrations.RemoveField(
            model_name='variablevalue',
            name='common_variable',
        ),
        migrations.RemoveField(
            model_name='variablevalue',
            name='custom_variable',
        ),
        migrations.AddField(
            model_name='variable',
            name='is_custom',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='CommonVariable',
        ),
        migrations.DeleteModel(
            name='CustomVariable',
        ),
    ]
