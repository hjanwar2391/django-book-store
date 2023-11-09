from django.shortcuts import render, redirect
from book.forms import BookForms
from . import models

# Create your views here.

def home(request):
    if request.method =="POST":
        book = BookForms(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
    else:
        book = BookForms()
    return render(request, './home/home.html', {'form': book})


def bookList(request):
    allBook = models.BookModels.objects.all()
    print(allBook)
    return render(request, './bookList/bookList.html', {'book':allBook})

def deleteBook(request, id):
    deleteBook = models.BookModels.objects.get(id).delete()
    return redirect('bookList')