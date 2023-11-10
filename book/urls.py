from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('book_list', views.bookList, name='bookList'),
    path('addBook/', views.addBook, name='addBook'),
    path('delete/<int:id>', views.deleteBook, name='deleteBook'),
    path('updateBook/<int:id>', views.updateBook, name="update")
]
