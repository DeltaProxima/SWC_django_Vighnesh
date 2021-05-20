from . import views
from django.urls import path

urlpatterns = [
    path('',views.wands,name='site-wands'),
]
