from django.contrib import admin
from . models import Category

# Register your models here.
class CategoryRegisterModel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name', )}
    list_display = ["category_name", "slug", "cat_image"]
    
admin.site.register(Category, CategoryRegisterModel)