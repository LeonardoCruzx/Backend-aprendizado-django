# Generated by Django 3.0 on 2019-12-12 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]