# Generated by Django 2.1.4 on 2019-01-16 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_input_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='input',
            name='active',
        ),
        migrations.AddField(
            model_name='input',
            name='disable',
            field=models.BooleanField(default=False, help_text='Check box to disable tracking'),
        ),
    ]
