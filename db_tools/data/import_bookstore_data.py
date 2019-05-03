import sys
import os



pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore_management_system.settings")

import django
django.setup()

from bookstore.models import BookStore
from db_tools.data.bookstore_data import raw_data

for bookstore_detail in raw_data:
	bookstore = BookStore()
	bookstore.store_name = bookstore_detail["store_name"]
	bookstore.address = bookstore_detail["address"]
	bookstore.introduction = bookstore_detail["introduction"]

	bookstore.save()

print("书店信息录入成功!")