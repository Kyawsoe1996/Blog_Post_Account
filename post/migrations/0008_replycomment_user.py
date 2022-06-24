# Generated by Django 3.2.7 on 2021-09-22 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_account_id'),
        ('post', '0007_auto_20210922_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='replycomment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='account.account'),
        ),
    ]
