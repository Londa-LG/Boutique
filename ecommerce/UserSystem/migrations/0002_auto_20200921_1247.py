# Generated by Django 3.1.1 on 2020-09-21 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserSystem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pic',
            new_name='picture',
        ),
    ]