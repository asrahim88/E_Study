from django.shortcuts import render
from book_management.models import Books
def home(request):
    searchBooks = request.GET.get('search_book')
    results = Books.objects.filter(book_title__icontains=searchBooks)
    print('Search box', results)
    return render(request, 'home.html')