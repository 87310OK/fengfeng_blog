# Generated by Django 3.2.10 on 2022-03-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, verbose_name='发送者邮箱')),
                ('content', models.TextField(verbose_name='发送的内容')),
            ],
            options={
                'verbose_name_plural': '邮件发送',
            },
        ),
    ]
