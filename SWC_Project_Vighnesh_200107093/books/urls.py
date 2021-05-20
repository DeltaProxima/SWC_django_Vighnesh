from . import views
from django.urls import path

urlpatterns = [
    path('',views.books,name='site-books'),
]