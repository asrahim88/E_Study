from django.urls import path
from . import views

urlpatterns = [
    path("", views.manage_book, name= 'manage_book')
]
