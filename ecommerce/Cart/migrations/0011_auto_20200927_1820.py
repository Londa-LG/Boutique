# Generated by Django 3.1.1 on 2020-09-27 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cart', '0010_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingdetails',
            name='order',
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]