from django.db import models


# Create your models here.
class BookStack(models.Model):
	# id = models.CharField(max_length=40, unique=True, verbose_name='id', null=True, default=None)
	stack_name = models.CharField(primary_key=True, max_length=30, verbose_name="书库")

	class Meta:
		verbose_name = "书库"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.stack_name