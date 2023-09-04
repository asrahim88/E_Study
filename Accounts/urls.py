from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.sign_up, name= 'signUp'),
    path("profile/", views.profile, name= 'profile'),
    path("signIn/", views.signIn, name= 'signIn'),
    path("signOut/", views.signOut, name= 'signOut'),
    path("delete_wish_book/<int:id>", views.delete_wish_book, name= 'delete_wish'),
]
