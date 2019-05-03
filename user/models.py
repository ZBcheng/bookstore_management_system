from django.db import models
from django.contrib.auth.models import User

from bookstack.models import BookStack

# Create your models here.
class UserStack(BookStack):
	user = models.OneToOneField(User, verbose_name="已购清单", on_delete=models.CASCADE)

	class Meta:
		verbose_name = "已购清单"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.user.get_username()