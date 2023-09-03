from django.contrib import admin
from . models import Books

# Register your models here.
class BooksRegisterModel(admin.ModelAdmin):
    list_display = ["book_title", "id", "ISBN", "author", "description", "images", "stock", "is_available", "genre", "first_pub", "modified_pub"]
admin.site.register(Books, BooksRegisterModel)