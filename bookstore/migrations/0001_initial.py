# Generated by Django 2.2 on 2019-04-25 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        ('bookstack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.IntegerField(default='000', primary_key=True, serialize=False, unique=True)),
                ('nick_name', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('password', models.CharField(default='000', max_length=128, verbose_name='密码')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='生日')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default=('male', '男'), max_length=6, verbose_name='性别')),
                ('address', models.CharField(default='', max_length=100, verbose_name='地址')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机')),
                ('image', models.ImageField(default='image/default.png', upload_to='image/%Y/%m')),
            ],
            options={
                'verbose_name': '管理员信息',
                'verbose_name_plural': '管理员信息',
            },
        ),
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('store_name', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='书店名')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='位置')),
                ('book_stack', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookstack.BookStack', verbose_name='书库')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookstore.Manager', verbose_name='管理员')),
                ('supplier', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.Supplier', verbose_name='供应商')),
            ],
            options={
                'verbose_name': '书店信息',
                'verbose_name_plural': '书店信息',
            },
        ),
    ]
