from django import forms


# 登陆表单
class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, min_length=5)


# 注册表单
class RegisterForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, min_length=5)
