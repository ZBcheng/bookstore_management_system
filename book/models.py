# Create your models here.
from django.db import models

from bookstack.models import BookStack

# Create your models here.
class Book(models.Model):
	book_name = models.CharField(primary_key=True, max_length=30, verbose_name="书名")
	publisher = models.CharField(max_length=30, verbose_name="出版社")
	writer = models.CharField(max_length=50, verbose_name="作者")
	price = models.IntegerField(verbose_name="价格")
	number = models.IntegerField(verbose_name="数量")
	book_stack = models.ForeignKey(BookStack, verbose_name="书库", on_delete=models.CASCADE, null=True, default=None)

	class Meta:
		app_label = "book"
		verbose_name = "书"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.book_name
