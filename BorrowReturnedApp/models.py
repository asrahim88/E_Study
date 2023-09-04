from django.db import models
from django.contrib.auth.models import User
from book_management.models import Books

# Create your models here.

class BorrowReturn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    is_returned = models.BooleanField(default=False)

class Review(models.Model):
    text = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.text