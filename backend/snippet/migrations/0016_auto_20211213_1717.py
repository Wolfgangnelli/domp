# Generated by Django 3.1.2 on 2021-12-13 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0015_auto_20211213_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecommercesnippetcustom',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ecommerce_snippet_custom', to='snippet.event'),
        ),
    ]
