# Generated by Django 2.2.1 on 2019-05-03 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_delete_customer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstack', '0001_initial'),
        ('user', '0003_auto_20190430_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStack',
            fields=[
                ('bookstack_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bookstack.BookStack')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='已购清单')),
            ],
            options={
                'verbose_name': '已购清单',
                'verbose_name_plural': '已购清单',
            },
            bases=('bookstack.bookstack',),
        ),
        migrations.DeleteModel(
            name='BaseUser',
        ),
    ]
