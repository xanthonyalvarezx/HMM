# Generated by Django 4.0 on 2022-05-27 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0002_register_delete_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='title',
        ),
    ]
