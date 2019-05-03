import sys
import os



pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore_management_system.settings")

import django
django.setup()

from bookstore.models import Manager
from db_tools.data.manager_data import raw_data

for manager_detail in raw_data:
	manager = Manager()
	manager.id = manager_detail['id']
	manager.nick_name = manager_detail['name']
	manager.password = manager_detail['password']
	manager.mobile = manager_detail['mobile']
	manager.address = manager_detail['address']

	manager.save()


print("管理员信息录入成功!")