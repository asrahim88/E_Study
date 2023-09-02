from django.urls import path
from . import views

urlpatterns = [
    path("", views.manage_book, name= 'manage_book'),
    path("category/<slug:category_slug>/", views.manage_book, name= 'category_wise'),
    path("/<slug:category_slug>/<slug:book_slug>/", views.bookDetails, name='book_details')
]
