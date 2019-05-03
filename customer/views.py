# from django.shortcuts import render
# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import authenticate, login, logout
# from django.views.generic.base import View
#
# from customer.models import Customer
# from bookstore.views import getBookStore
#
# # Create your views here.
#
# current_user = None # 当前登录的用户
#
#
# class LoginView(View):
# 	def get(self, request):
# 		return render(request, 'login.html', {})
#
# 	def post(self, request):
# 		nick_name = request.POST.get("nick_name", "")
# 		pass_word = request.POST.get("password", "")
# 		user = Customer.objects.get(nick_name=nick_name)
# 		if user is not None:
# 			current_user = user
# 			return getBookStore(request, current_user)
# 		else:
# 			return render(request, "login.html", {'msg': '用户不存在'})
#
#
# class RegisterView(View):
# 	def get(self, request):
# 		return render(request, "register.html")
#
# 	def post(self, request):
# 		nick_name = request.POST.get("nick_name")
# 		pass_word = request.POST.get("password")
# 		email = request.POST.get("email")
# 		birthday = request.POST.get("birthday")
# 		name = request.POST.get("name")
# 		mobile = request.POST.get("mobile")
# 		user = Customer.objects.create(name=name, nick_name=nick_name, password=pass_word, email=email, birthday=birthday, mobile=mobile)
# 		user.save()
# 		current_user = user
# 		if user is not None:
# 			return getBookStore(request, current_user)
# 		else:
# 			return render(request, "login.html", {'msg': '登录错误'})
#
#
# def userLogout(request):
# 	current_user = None
# 	return getBookStore(request, current_user)
