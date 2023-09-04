from django.db import models
from django.contrib.auth.models import User
from book_management.models import Books

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wish_book = models.ForeignKey(Books, on_delete=models.CASCADE)