# Generated by Django 3.2.7 on 2021-09-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_replycomment_reply_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='replycomment',
            name='likes_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
