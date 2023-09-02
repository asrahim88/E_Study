from django.contrib import admin
from . models import Books

# Register your models here.
class BooksRegisterModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('book_title', )}
    
    list_display = ["book_title", "ISBN", "author",  "slug", "description", "images", "stock", "is_available", "genre", "first_pub", "modified_pub"]
admin.site.register(Books, BooksRegisterModel)