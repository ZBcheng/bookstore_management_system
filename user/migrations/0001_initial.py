# Generated by Django 2.2 on 2019-04-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.IntegerField(default='', primary_key=True, serialize=False, unique=True)),
                ('nick_name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('password', models.CharField(default='000', max_length=128, verbose_name='密码')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default=('male', '男'), max_length=6, verbose_name='性别')),
                ('address', models.CharField(default='', max_length=100, verbose_name='地址')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]
