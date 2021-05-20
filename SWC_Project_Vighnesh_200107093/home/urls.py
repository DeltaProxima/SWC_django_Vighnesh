from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='site-home'),
    path('wands',views.wands,name='site-wands'),
    path('brooms',views.brooms,name='site-brooms')
]
