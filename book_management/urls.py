from django.urls import path, reverse
from . import views

urlpatterns = [
    path("", views.manage_book, name= 'manage_book'),
    path("add_books/", views.add_books, name= 'add_books'),
    path("category/<slug:category_slug>/", views.manage_book, name= 'category_wise'),
    path("category/<slug:category_slug>/<slug:book_slug>/", views.bookDetails, name='book_details')
]