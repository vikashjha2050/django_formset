# Generated by Django 2.0.3 on 2019-01-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subexam',
            name='institute',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
