# Generated by Django 3.1.2 on 2020-12-26 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201226_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='present_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
