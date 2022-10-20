# Generated by Django 4.1.2 on 2022-10-18 16:05

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('courses', '0007_remove_subject_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('text', 'video', 'image', 'file', 'exam')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='course',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]