from django.shortcuts import render
from book_management.models import Books
from BorrowReturnedApp.models import Review

def home(request):
    # Book Searching start
    search_item = request.GET.get("search_book")
    if search_item:
       books = Books.objects.filter(book_title__icontains = search_item)
    else:
        books = Books.objects.all()
    # Book Searching End
    
    # Showing all the reviews 
    reviews = Review.objects.all()
    return render(request, 'home.html', {"books": books, "search_book": search_item, "reviews": reviews})