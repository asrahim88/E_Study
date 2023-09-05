from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from book_management.models import Books
from .models import BorrowReturn
from .review_forms import ReviewForm
from django.shortcuts import get_object_or_404
 
   
def borrow_book(request, id):
        if request.user.is_authenticated:
            try:
                borrowed_book = BorrowReturn.objects.get(user=request.user, book_id__id=id, is_returned=False)
                print(borrowed_book)
                
                return redirect("manage_book")
            except ObjectDoesNotExist:
                   
                try:
                    book = Books.objects.get(id=id, stock__gt=0)
                except ObjectDoesNotExist:
                    return redirect("manage_book")
                
                borrow_return_instance = BorrowReturn(
                    user=request.user,
                    book_id=book,  
                    is_returned = False,  
                )
                borrow_return_instance.save()
                
                book.stock -=1
                book.save() 
            return redirect("manage_book")  
        else:
            return redirect("signIn")


def show_borrowed_book_list(request):
    if request.user.is_authenticated and (not request.user.is_superuser and not request.user.is_staff):
        user = request.user
        borrowed_books= BorrowReturn.objects.filter(user=user, is_returned=False)
        
        
        return render(request, "showBorrowList.html", {"borrow_books": borrowed_books})
    else:
        return redirect("home")


def return_book(request, id):
    if request.user.is_authenticated:
        book = get_object_or_404(Books, id=id)
        book.stock += 1
        book.save()
        
        return_books = get_object_or_404(BorrowReturn, book_id__id=id, user=request.user)
        return_books.is_returned = True
        return_books.delete()
        
        return redirect("borrow_list")
    else:
        return redirect("home")


def create_review(request, id):  
    if request.user.is_authenticated:
        if not request.user.is_superuser and not request.user.is_staff:
            book = Books.objects.get(id=id)
    
            if request.method == 'POST':
                form = ReviewForm(request.POST)
                if form.is_valid():
                    review = form.save(commit=False)
                    review.user = request.user
                    review.book = book  
                    review.save()
                    return redirect('home')  
            else:
                form = ReviewForm()

            return render(request, 'review_form.html', {'form': form})
        else:
            return redirect("home")
    else:
        return redirect("home")
