# Generated by Django 2.0.3 on 2019-01-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20190103_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subexam',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
