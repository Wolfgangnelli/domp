# Generated by Django 3.1.2 on 2022-02-24 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_auto_20220210_1804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentvariable',
            options={'ordering': ['-pk'], 'verbose_name': 'Document variable', 'verbose_name_plural': 'Document variables'},
        ),
    ]
