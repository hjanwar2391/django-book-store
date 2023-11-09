from django import forms
from book.models import BookModels

class BookForms(forms.ModelForm):
    class Meta:
        model = BookModels
        fields = '__all__'
    
