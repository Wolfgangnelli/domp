# Generated by Django 3.1.2 on 2022-01-18 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_initialsnippetvariable_old_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialsnippetvariable',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='initial_snippet_variable', to='base.variabletype'),
        ),
    ]
