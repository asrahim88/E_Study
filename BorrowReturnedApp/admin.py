from django.contrib import admin
from .models import BorrowReturn, Review
# Register your models here.

class BorrowReturnRegisterAdmin(admin.ModelAdmin):
    list_display = ["user", "book_id", "is_returned"]

class ReviewRegisterAdmin(admin.ModelAdmin):
    list_display = ['text', "date", "user", "book"]

admin.site.register(BorrowReturn, BorrowReturnRegisterAdmin)
admin.site.register(Review, ReviewRegisterAdmin)