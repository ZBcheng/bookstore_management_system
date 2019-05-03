from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from bookstore.views import getBookStore, enterBookStore

# Create your views here.
class LoginView(View):
	def get(self, request):
		return render(request, 'login.html', {})

	def post(self, request):
		user_name = request.POST.get("username", "")
		pass_word = request.POST.get("password", "")
		user = authenticate(username=user_name, password=pass_word)
		if user is not None:
			login(request, user)
			return render(request, "index.html")
		else:
			return getBookStore(request)


class RegisterView(View):
	def get(self, request):
		return render(request, 'register.html')

	def post(self, request):
		user_name = request.POST.get("username", "")
		pass_word = request.POST.get("password", "")
		email = request.POST.get("email", "")
		birthday = request.POST.get("birthday", "")

		user = User.objects.create(username=user_name, password=pass_word, email=email)
		user.save()
		login(request, user)
		return getBookStore(request)


def userLogout(request):
	logout(request)
	return getBookStore(request)


def qujiangBookStore(request):
	return enterBookStore(request, '曲江书城')