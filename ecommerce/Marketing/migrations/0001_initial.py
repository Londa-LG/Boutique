# Generated by Django 3.1.1 on 2020-09-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Emails',
            },
        ),
    ]
