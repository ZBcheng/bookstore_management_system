from django.shortcuts import render
from django.views.generic.base import View

from .models import BookStore
from .models import BookStoreStack
from book.models import Book, BookStack
# from supplier.models import Supplier
# from customer.models import CurrentUser

# Create your views here.


def getBookStore(request):
	'''没错，我膨胀了，我就是想用中文当变量名，咋地'''
	曲江书城 = BookStore.objects.get(store_name="曲江书城") # 西安 张毕成
	言几又 = BookStore.objects.get(store_name="言几又 迈科中心") # 西安 周松松
	中信书店 = BookStore.objects.get(store_name="中信书店") # 大连 崔鹏
	止间书店 = BookStore.objects.get(store_name="止间书店") # 长沙 刘逵

	return render(request, "index.html",
	              {
		              '曲江书城': 曲江书城,
		              '言几又': 言几又,
		              '中信书店': 中信书店,
		              '止间书店': 止间书店,
	              }
	              )


# def buyBooks(request, book_name, supplier_name):
# 	supplier = Supplier.objects.get(supplier_name=supplier_name)
# 	book_stack_supplier = supplier.book_stack


def enterBookStore(request, store_name):
	store = BookStore.objects.get(store_name=store_name)  # 西安 张毕成
	bookstore_stack = BookStoreStack.objects.get(bookstore=store)
	store_stack_name = store_name + '书库'
	books = Book.objects.filter(book_stack__stack_name=store_stack_name)


	if store_name == "曲江书城":
		page = "qujiang_bookstore",
	elif store_name == "言几又":
		page = "yanijyou_bookstore"
	elif store_name == "中信书店":
		page = "zhongxinshudian_bookstore"
	elif store_name == "止间书店":
		page = "zhijianshudian_bookstore"



	return render(request, "%s.html" % page, {'store': store, 'bookstore_stack': bookstore_stack, 'books': books})