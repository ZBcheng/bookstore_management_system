from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Book
from bookstack.models import BookStack


# Register your models here.
class BookAdmin(admin.ModelAdmin):
	list_display = ['book_name', 'publisher', 'writer', 'price', 'number', '所属书库']
	search_fields = ['book_name', 'publisher', 'writer']
	list_filter = ['publisher', 'writer']

	def 所属书库(self, obj):
		return obj.book_stack.stack_name


admin.site.register(Book, BookAdmin)