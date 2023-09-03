from django import forms
from .models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_title', "id", 'ISBN', 'author', 'description', 'images', 'stock', 'is_available', 'genre']
