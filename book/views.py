from django.shortcuts import render
from django.views.generic.base import View

from .models import Book
# Create your views here.

def get(request):
	book = Book.objects.get(book_name="万历十五年")
	return render(request, "index.html", {'book_name': book.book_name})