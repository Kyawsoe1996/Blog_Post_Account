# Generated by Django 3.2.7 on 2021-09-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_replycomment_reply_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replycomment',
            name='reply_text',
            field=models.TextField(blank=True),
        ),
    ]
