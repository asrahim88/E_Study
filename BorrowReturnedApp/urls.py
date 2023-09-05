from django.urls import path
from . import views
urlpatterns = [
    path("borrow_list/", views.show_borrowed_book_list, name= 'borrow_list'),
    path("<int:id>/", views.borrow_book, name='borrow'),
    path("review/<int:id>/", views.create_review, name='review'),
    path("return_book/<int:id>/", views.return_book, name='book_return'),
]
