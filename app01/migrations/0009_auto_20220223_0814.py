# Generated by Django 3.2.10 on 2022-02-23 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20220213_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='moods',
            name='addr',
            field=models.JSONField(null=True, verbose_name='用户地址信息'),
        ),
        migrations.AddField(
            model_name='moods',
            name='ip',
            field=models.GenericIPAddressField(default='120.228.2.238', verbose_name='ip地址'),
        ),
    ]
