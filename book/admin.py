from django.contrib import admin
from book.models import BookModels

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display =['name', 'title', 'author']

admin.site.register(BookModels, BookAdmin)