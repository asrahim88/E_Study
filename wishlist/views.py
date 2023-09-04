from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from BorrowReturnedApp.models import BorrowReturn
from book_management.models import Books
from . models import WishList
# Create your views here.

def add_to_wishList(request, id):
    if request.user.is_authenticated:
        try:
            wishListedBook = WishList.objects.get(wish_book__id=id)
            print(wishListedBook)

            return redirect("manage_book")
        except ObjectDoesNotExist:
            book = Books.objects.get(id=id)
            user = request.user 
                
            wish_list_instance = WishList(
                user=user,
                wish_book=book,  
            )
            wish_list_instance.save()
            return redirect("manage_book")
    else:
        return redirect("signIn")


# def show_wish_list(request):
    
#     return redirect("profile")