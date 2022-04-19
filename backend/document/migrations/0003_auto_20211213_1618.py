# Generated by Django 3.1.2 on 2021-12-13 16:18

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0014_remove_gaeventsnippetcustom_event'),
        ('document', '0002_auto_20211213_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='eco_snippet_custom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section', to='snippet.ecommercesnippetcustom'),
        ),
        migrations.AddField(
            model_name='section',
            name='eco_snippet_std',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section', to='snippet.ecommercesnippetstd'),
        ),
        migrations.AddField(
            model_name='section',
            name='ga_event_snippet_custom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section', to='snippet.gaeventsnippetcustom'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('url', models.CharField(blank=True, max_length=255)),
                ('section', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='document.section')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
