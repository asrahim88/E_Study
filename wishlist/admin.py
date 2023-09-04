from django.contrib import admin
from .models import WishList

# Register your models here
class WishListRegisterAdmin(admin.ModelAdmin):
    list_display = ["user", "wish_book"]
admin.site.register(WishList, WishListRegisterAdmin)