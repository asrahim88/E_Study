from django.shortcuts import render, redirect
from django.contrib import messages
from . import signUp_forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from wishlist.models import WishList
# Create your views here.


def profile(request):
    if request.user.is_authenticated:
        wishListBook = WishList.objects.filter(user=request.user)
        return render(request, 'profile.html', {"wishList": wishListBook})
    else:
        return redirect("signIn")
    
def delete_wish_book(request, id):
    if request.user.is_authenticated:
        delete_wished_book = WishList.objects.get(user=request.user, wish_book__id=id)
        delete_wished_book.delete()
        return redirect("profile")
    else:
        return redirect("home")
    
def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = signUp_forms.UserRegister(request.POST)
            if form.is_valid():
                messages.success(request, "Account Created Successfully")
                form.save()
                return redirect("signIn")
        else:
            form = signUp_forms.UserRegister()
            
        return render(request, 'sign_up.html', {"form": form})
    else:
        return redirect("profile")

def signIn(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid():
                userName = form.cleaned_data["username"]
                userPassword = form.cleaned_data["password"]
                user = authenticate(username = userName, password = userPassword )
                if user is not None:
                    login(request, user)
                    return redirect("profile")
        else:
            form = AuthenticationForm()
        return render(request, "signIn.html", {"form": form})
    else:
        return redirect("profile")

def signOut(request):
    logout(request)
    return redirect("signIn")
