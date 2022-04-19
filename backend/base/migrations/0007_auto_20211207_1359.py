# Generated by Django 3.1.2 on 2021-12-07 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0001_initial'),
        ('base', '0006_variablevalue_variable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customfield',
            name='eco_snippet',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='eco_snippet',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='event',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='ga_event_snippet',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='init_snippet',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='section',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
        migrations.AlterField(
            model_name='snippetvariable',
            name='eco_snippet',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippet_variable', to='snippet.ecommercesnippet'),
        ),
        migrations.AlterField(
            model_name='snippetvariable',
            name='ga_event_snippet',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippet_variable', to='snippet.gaeventsnippet'),
        ),
        migrations.AlterField(
            model_name='snippetvariable',
            name='init_snippet',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippet_variable', to='snippet.initialsnippet'),
        ),
        migrations.DeleteModel(
            name='CustomField',
        ),
        migrations.DeleteModel(
            name='EcommerceSnippet',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='GAeventSnippet',
        ),
        migrations.DeleteModel(
            name='InitialSnippet',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
