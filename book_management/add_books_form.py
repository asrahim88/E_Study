from django import forms
from .models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_title', 'ISBN', 'author', 'slug', 'description', 'images', 'stock', 'is_available', 'genre']
