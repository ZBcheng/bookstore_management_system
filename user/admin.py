from django.contrib import admin

from .models import UserStack

# Register your models here.

class UserStackAdmin(admin.ModelAdmin):
	list_display = ['stack_name']
	list_filter = ['stack_name']
	search_fields = ['stack_name']

admin.site.register(UserStack, UserStackAdmin)