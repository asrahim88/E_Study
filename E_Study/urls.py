from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('account/', include("Accounts.urls")),
]
