from django.db import models

from supplier.models import Supplier
from bookstack.models import BookStack

# Create your models here.
class Manager(models.Model):
	# id = models.IntegerField(primary_key=True, unique=True, default="000")
	# USERNAME_FIELD = 'id'


	nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
	password = models.CharField(max_length=128, verbose_name="密码", default='000')
	birthday = models.DateTimeField(verbose_name='生日', null=True, blank=True)
	gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default=('male', '男'), verbose_name="性别")
	address = models.CharField(max_length=100, default='', verbose_name='地址')
	mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机')
	image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100)

	class Meta:
		verbose_name = '管理员信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.nick_name



class BookStore(models.Model):
	store_name = models.CharField(primary_key=True, max_length=30, verbose_name="书店名")
	address = models.CharField(max_length=100, verbose_name="位置", null=True)
	introduction = models.TextField(verbose_name="简介", default="")
	supplier = models.ForeignKey(Supplier, verbose_name="供应商", on_delete=models.CASCADE, null=True, default=None)


	class Meta:
		verbose_name = "书店信息"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.store_name


class BookStoreStack(BookStack):
	bookstore = models.ForeignKey(BookStore, verbose_name="所属书店", on_delete=models.CASCADE)

	class Meta:
		verbose_name = "书店书库"
		verbose_name_plural = verbose_name