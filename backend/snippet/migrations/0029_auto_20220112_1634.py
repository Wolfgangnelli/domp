# Generated by Django 3.1.2 on 2022-01-12 16:34

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20220103_0903'),
        ('snippet', '0028_auto_20220105_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialSnippetVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Initial snippet variable',
                'verbose_name_plural': 'Initial snippet variables',
            },
        ),
        migrations.RemoveField(
            model_name='initialsnippet',
            name='name',
        ),
        migrations.RemoveField(
            model_name='initialsnippet',
            name='value',
        ),
        migrations.CreateModel(
            name='InitialSnippetVariableValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('initial_snippet_variable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initial_snippet_variable_value', to='snippet.initialsnippetvariable')),
            ],
            options={
                'verbose_name': 'Initial snippet variable value',
                'verbose_name_plural': 'Initial snippet variable values',
            },
        ),
        migrations.AddField(
            model_name='initialsnippetvariable',
            name='initial_snippet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initial_snippet_variable', to='snippet.initialsnippet'),
        ),
        migrations.AddField(
            model_name='initialsnippetvariable',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='initial_snippet_variable', to='base.variabletype'),
        ),
    ]
