from django.contrib import admin

from .models import BookStore
from .models import BookStoreStack
from .models import Manager


# Register your models here.

# 书店
class BookStoreAdmin(admin.ModelAdmin):
	list_display = ['store_name', 'address']
	search_fields = ['store_name', 'address']
	list_filter = ['store_name', 'address']


# 书店书库
class BookStoreStackAdmin(admin.ModelAdmin):
	list_display = ['stack_name']
	search_fields = ['stack_name']


# 书店管理员
class ManagerAdmin(admin.ModelAdmin):
	list_display = ['nick_name', 'birthday', 'gender', 'address', 'mobile', 'image']
	search_fields = ['nick_name', 'birthday', 'gender', 'address', 'mobile']
	list_filter = ['nick_name', 'birthday', 'gender', 'address', 'mobile', 'image']


admin.site.register(BookStore, BookStoreAdmin)
admin.site.register(BookStoreStack, BookStoreStackAdmin)
admin.site.register(Manager, ManagerAdmin)