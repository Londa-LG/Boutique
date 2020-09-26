# Generated by Django 3.1.1 on 2020-09-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0005_auto_20200926_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingdetails',
            name='address_line1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='address_line2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='state_or_country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='town_or_city',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
