# Generated by Django 4.1.2 on 2022-10-18 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_subject_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='grade',
        ),
    ]
