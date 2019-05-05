from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from bookstore.views import getBookStore, enterBookStore
from book.models import Book
from bookstore.models import BookStore, BookStoreStack
from supplier.models import SupplierStack

# Create your views here.

def adminBookStore(request, books):
	return render(request, 'supplier.html', {'books': books})


class SupplierView(View):
	def get(self, request):
		books = Book.objects.filter(book_stack__stack_name='中国卖书有限公司书库')
		return adminBookStore(request, books)

	def post(self, request):
		books = Book.objects.filter(book_stack__stack_name='中国卖书有限公司书库')
		book_name = request.POST.get("book_name", "")
		store_name = request.POST.get("store_name", "")
		if store_name == "言几又 迈科中心":
			stack_name = "言几又书库"
		else:
			stack_name = store_name + "书库"
		bookstore_stack = BookStoreStack.objects.get(stack_name=stack_name)
		supplier_stack = SupplierStack.objects.get(stack_name='中国卖书有限公司书库')
		book = Book.objects.get(book_name=book_name)
		book.book_stack = bookstore_stack
		book.save()

		return adminBookStore(request, books)

class AdminLoginView(View):
	def get(self, request):
		return render(request, 'adminlogin.html')

	def post(self, request):
		store_name = request.POST.get("store_name", "")
		pass_word = request.POST.get("password", "")

		books = Book.objects.filter(book_stack__stack_name='中国卖书有限公司书库')
		bookstore = BookStore.objects.get(store_name=store_name)
		print(books)
		if pass_word == 'admin':
			return render(request, 'supplier.html', {'store': bookstore, 'books': books})



class LoginView(View):
	def get(self, request):
		return render(request, 'login.html', {})


	def post(self, request):
		user_name = request.POST.get("username", "")
		pass_word = request.POST.get("password", "")
		user = User.objects.get(username=user_name)
		if user is not None:
			login(request, user)
			return getBookStore(request)
		else:
			return getBookStore(request)


class RegisterView(View):
	def get(self, request):
		return render(request, 'register.html')

	def post(self, request):
		name = request.POST.get("name", "")
		user_name = request.POST.get("username", "")
		pass_word = request.POST.get("password", "")
		email = request.POST.get("email", "")
		birthday = request.POST.get("birthday", "")
		mobile = request.POST.get("mobile", "")

		user = User.objects.create(name=name, username=user_name, password=pass_word, email=email, mobile=mobile, birthday=birthday)
		user.save()
		login(request, user)
		return getBookStore(request)


def userLogout(request):
	logout(request)
	return getBookStore(request)


def qujiangBookStore(request):
	return enterBookStore(request, '曲江书城')


def yanjiyouBookStore(request):
	return enterBookStore(request, '言几又 迈科中心')


def zhongxinBookStore(request):
	return enterBookStore(request, '中信书店')


def zhijianBookStore(request):
	return enterBookStore(request, '止间书店')


class qujiangBooksView(View):
	def get(self, request):
		return qujiangBookStore(request)

	def post(self, request):
		book_name = request.POST.get("book_name", "")
		book = Book.objects.get(book_name=book_name)
		book.number -= 1
		book.save()

		return qujiangBookStore(request)


class yanjiyouBooksView(View):
	def get(self, request):
		return yanjiyouBookStore(request)

	def post(self, request):
		book_name = request.POST.get("book_name", "")
		book = Book.objects.get(book_name=book_name)
		book.number -= 1
		book.save()

		return yanjiyouBookStore(request)


class zhongxinBooksView(View):
	def get(self, request):
		return zhongxinBookStore(request)

	def post(self, request):
		book_name = request.POST.get("book_name", "")
		book = Book.objects.get(book_name=book_name)
		book.number -= 1
		book.save()

		return zhongxinBookStore(request)


class zhijianBooksView(View):
	def get(self, request):
		return zhijianBookStore(request)

	def post(self, request):
		book_name = request.POST.get("book_name", "")
		book = Book.objects.get(book_name=book_name)
		book.number -= 1
		book.save()

		return zhijianBookStore(request)
