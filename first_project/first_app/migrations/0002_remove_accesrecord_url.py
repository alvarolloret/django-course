# Generated by Django 2.0.2 on 2018-05-16 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesrecord',
            name='url',
        ),
    ]
