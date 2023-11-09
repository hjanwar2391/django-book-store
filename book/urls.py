from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('book_list', views.bookList, name='bookList'),
    path('delete/<int:id>', views.deleteBook, name='deleteBook')
]
