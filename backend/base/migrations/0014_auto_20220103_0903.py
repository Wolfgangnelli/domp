# Generated by Django 3.1.2 on 2022-01-03 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0024_auto_20220103_0903'),
        ('base', '0013_auto_20220101_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippetvariable',
            name='ga4_eco_snippet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippet_variable', to='snippet.ecommercesnippetga4'),
        ),
        migrations.AddField(
            model_name='snippetvariable',
            name='ga4_eco_snippet_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippet_variable', to='snippet.ecommercesnippettemplatega4'),
        ),
    ]
