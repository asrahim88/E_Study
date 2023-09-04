from django.db import models
from books_category.models import Category
# Create your models here.
class Books(models.Model):
    book_title = models.CharField(max_length=300, unique=True)
    id= models.PositiveIntegerField(primary_key=True)
    ISBN = models.CharField(max_length=50, unique= True)
    author = models.CharField(max_length=50, default='author')
    description = models.TextField(max_length=500, blank=True)
    images = models.ImageField(upload_to= 'photos/books')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    genre = models.ForeignKey(Category, on_delete=models.CASCADE)
    first_pub =models.DateField(auto_now_add=True, null=True, blank=True)
    modified_pub = models.DateField(auto_now=True) 
    
    def __str__(self) -> str:
        return self.book_title