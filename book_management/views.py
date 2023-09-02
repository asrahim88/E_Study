from django.shortcuts import render, get_object_or_404
from . models import Books
from book_management.models import Category

# Create your views here.
def manage_book(request, category_slug= None):
    
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        books = Books.objects.filter(is_available = True, genre = category)
    else:
        books = Books.objects.filter(is_available = True)   
    categories = Category.objects.all()
    
    context = {"books": books, "categories": categories}
    return render(request, 'book_manage.html', context)

def bookDetails(request, category_slug, book_slug):
    single_book = Books.objects.get(slug= book_slug, genre__slug = category_slug)
    print('image',single_book)
    return render(request, 'book_details.html', {"book_details": single_book})