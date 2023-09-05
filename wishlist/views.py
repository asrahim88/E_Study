from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from book_management.models import Books
from .models import WishList

def add_to_wishList(request, id):
    if request.user.is_authenticated:
        try:
            wishListedBook = WishList.objects.get(user=request.user, wish_book__id=id)
            
            print(wishListedBook)
            return redirect("manage_book")
        
        except ObjectDoesNotExist:
            book = Books.objects.get(id=id)
                
            wish_list_instance = WishList(
                user=request.user,
                wish_book=book,  
            )
            wish_list_instance.save()
            return redirect("manage_book")
    else:
        return redirect("signIn")







