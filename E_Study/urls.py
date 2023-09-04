from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name= 'home'),
    path('admin/', admin.site.urls),
    path('account/', include("Accounts.urls")),
    path('books/', include("book_management.urls")),
    path('category/', include("books_category.urls")),
    path('borrow/', include("BorrowReturnedApp.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
