import sys
import os



pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore_management_system.settings")

import django
django.setup()

from book.models import Book
from supplier.models import Supplier, SupplierStack
from db_tools.data.book_data import raw_data


# 先创建书库，将book_data中的所有书添加到这个书库中

book_stack = SupplierStack()
book_stack.stack_name = "中国卖书有限公司书库"

supplier = Supplier()
supplier.supplier_name = "中国卖书有限公司"
supplier.id = 1
book_stack.supplier = supplier

supplier.save()
book_stack.save()


print("书库信息录入成功!")

for book_detail in raw_data:
	book = Book()
	book.book_name = book_detail["book_name"]
	book.publisher = book_detail["publisher"]
	book.writer = book_detail["writer"]
	book.price = book_detail["price"]
	book.number = book_detail["number"]
	book.book_stack = book_stack;
	book.save()

print("图书信息录入成功!")