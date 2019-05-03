# Generated by Django 2.2 on 2019-04-30 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstack', '0001_initial'),
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookstore',
            name='book_stack',
        ),
        migrations.RemoveField(
            model_name='bookstore',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='last_login',
        ),
        migrations.AddField(
            model_name='bookstore',
            name='introduction',
            field=models.TextField(default='', verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='BookStoreStack',
            fields=[
                ('bookstack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookstack.BookStack')),
                ('bookstore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.BookStore', verbose_name='所属书店')),
            ],
            options={
                'verbose_name': '书店书库',
                'verbose_name_plural': '书店书库',
            },
            bases=('bookstack.bookstack',),
        ),
    ]
