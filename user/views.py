from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from bookstore.views import getBookStore, enterBookStore
from book.models import Book

# Create your views here.
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


class buyBooksView(View):
	def get(self, request):
		return qujiangBookStore(request)

	def post(self, request):
		book_name = request.POST.get("book_name", "")
		book = Book.objects.get(book_name=book_name)
		book.number -= 1
		book.save()

		return qujiangBookStore(request)


