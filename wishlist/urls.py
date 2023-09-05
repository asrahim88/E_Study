from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/", views.add_to_wishList, name='add_to_wish_list'),
]
