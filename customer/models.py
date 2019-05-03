from django.db import models


# Create your models here.

# class BaseUser(models.Model):
# 	name = models.CharField(max_length=30, verbose_name="姓名")
# 	nick_name = models.CharField(max_length=30, verbose_name="昵称", primary_key=True)
# 	password = models.CharField(max_length=50, verbose_name="密码", null=False)
# 	gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default=('male', '男'), verbose_name="性别")
# 	birthday = models.DateTimeField(verbose_name="生日", null=False)
# 	address = models.CharField(max_length=100, verbose_name="地址", null=True, blank=True)
# 	mobile = models.CharField(max_length=15, verbose_name="电话", unique=True)
# 	email = models.EmailField(verbose_name="邮箱")
#
# 	class Meta:
# 		verbose_name = '用户'
# 		verbose_name_plural = verbose_name
#
# 	def __str__(self):
# 		return self.nick_name

#
# class Customer(BaseUser):
#
# 	class Meta:
# 		verbose_name = "用户"
# 		verbose_name_plural = verbose_name
#
# 	def __str__(self):
# 		return self.nick_name