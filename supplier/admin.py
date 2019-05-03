from django.contrib import admin

from .models import Supplier
from .models import SupplierStack

# Register your models here.

# 供应商
class SupplierAdmin(admin.ModelAdmin):
	list_display = ['supplier_name']
	search_fields = ['supplier_name']
	list_filter = ['supplier_name']

	def 子书库(self, obj):
		'''函数名还能用中文?真的🐂🍺'''
		return obj.child_supplier.stack_name


# 供应商书库
class SupplierStackAdmin(admin.ModelAdmin):
	list_display = ['stack_name']
	search_fields = ['stack_name']
	list_filter = ['stack_name']


admin.site.register(SupplierStack, SupplierStackAdmin)
admin.site.register(Supplier, SupplierAdmin)