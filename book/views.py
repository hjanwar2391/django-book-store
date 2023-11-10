from django.shortcuts import render, redirect
from book.forms import BookForms
from . import models

# Create your views here.

def home(request):
    book = models.BookModels.objects.all()
    return render(request, './home/home.html',{'book':book})

def addBook(request):
    if request.method =="POST":
        book = BookForms(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
    else:
        book = BookForms()
    return render(request, './addBook/addBook.html', {'form': book})

def bookList(request):
    allBook = models.BookModels.objects.all()
    print(allBook)
    return render(request, './bookList/bookList.html', {'book':allBook})

def updateBook(request, id):
    book = models.BookModels.objects.get(pk = id)
    form = BookForms(instance = book)
    if request.method =="POST":
        books = BookForms(request.POST, instance=book)
        if books.is_valid():
            books.save()
            return redirect('bookList')
    else:
        book = BookForms()   
    return render(request, './addBook/addBook.html', {'form':form})

def deleteBook(request, id):
    deleteBook = models.BookModels.objects.get(pk=id).delete()
    return redirect('bookList')


