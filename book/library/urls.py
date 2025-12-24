from django.urls import path
from .views import *

urlpatterns = [
    path('contact/',contact_view,name='contact'),
    path('create/',create_book,name='create_book'),
    path('list/',list_books,name='list_books'),
]