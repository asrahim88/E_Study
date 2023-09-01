from django.shortcuts import render, redirect
from django.contrib import messages
from . import signUp_forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {"user": request.user})
    else:
        return redirect("signIn")

def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = signUp_forms.UserRegister(request.POST)
            if form.is_valid():
                messages.success(request, "Account Created Successfully")
                form.save()
                print(form.cleaned_data)
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
