from django.shortcuts import render

# Create your views here.
def manage_book(request):
    books = [1,2,3,4,5,6,7,8,9,10]
    return render(request, 'book_manage.html', {"books": books})