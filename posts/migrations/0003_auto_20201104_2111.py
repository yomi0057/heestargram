# Generated by Django 3.1.2 on 2020-11-04 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201104_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='User',
            new_name='user',
        ),
    ]