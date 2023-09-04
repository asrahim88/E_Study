from django.shortcuts import render, redirect, get_object_or_404
from book_management.models import Books
from .models import BorrowReturn
from .review_forms import ReviewForm

def borrow_book(request, id):
        if request.user.is_authenticated:
            book = Books.objects.get(id=id)
            user = request.user 
            borrow_return_instance = BorrowReturn(
                user=user,
                book_id=book,  
                is_returned = False,  
            )
            borrow_return_instance.save()
            
            book.stock -=1
            book.save()
            
            
            return redirect("manage_book")  
        else:
            return redirect("signIn")

def show_borrow_book_list(request):
    user = request.user
    borrow_book_list= BorrowReturn.objects.filter(user = user)
    
    
    return render(request, "showBorrowList.html", {"borrow_books": borrow_book_list})



 
def return_book(request, id):
    
    book = Books.objects.get(id=id)
    book.stock +=1
    book.save()
    
    borrow_books = BorrowReturn.objects.filter(book_id__id=id, user=request.user)
    
    for borrow_book in borrow_books:
        borrow_book.is_returned = True
        borrow_book.save()
    
    return redirect("borrow_list")

def create_review(request, id):  
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
