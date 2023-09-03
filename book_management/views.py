from django.shortcuts import render, redirect, get_object_or_404
from . models import Books
from book_management.models import Category
from .add_books_form import BooksForm

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
    # working code start
    bookDetails = Books.objects.get(slug= book_slug, genre__slug = category_slug)
    print(bookDetails)
    # working code end
    return render(request, 'book_details.html', {"book_details": bookDetails})


def add_books(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BooksForm()
    return render(request, 'books_add_form.html', {'form': form})