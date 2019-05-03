from django.db import models

from django.db import models

from bookstack.models import BookStack

# Create your models here.

# 供应商
class Supplier(models.Model):
	supplier_name = models.CharField(max_length=40, verbose_name="供应商名")

	class Meta:
		verbose_name = "供应商"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.supplier_name


class SupplierStack(BookStack):
	supplier = models.ForeignKey(Supplier, verbose_name="所属供应商", on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name = "供应商书库"
		verbose_name_plural = verbose_name