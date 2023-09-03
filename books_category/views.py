from django.shortcuts import render, redirect


from .books_category_forms import CategoryForm

def add_category(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            form = CategoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("home") 
        else:
            form = CategoryForm()
        return render(request, 'category_forms.html', {'form': form})
    else:
        return redirect("signIn")

