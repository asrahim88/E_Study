from django.shortcuts import render, redirect

# Create your views here.
# views.py

from .books_category_forms import CategoryForm

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home") 
    else:
        form = CategoryForm()
    return render(request, 'category_forms.html', {'form': form})
