from django.urls import path
from . import views

urlpatterns = [
    # path("show_wish_list", views.show_wish_list, name='show_wish_list'),
    path("<int:id>/", views.add_to_wishList, name='add_to_wish_list'),
]
