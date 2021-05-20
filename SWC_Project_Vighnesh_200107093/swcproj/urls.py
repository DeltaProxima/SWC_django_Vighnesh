"""swcproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from home import views as home_views
from orders import views as orders_views
from wands import views as wand_views
from books import views as book_views
from brooms import views as brooms_views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('register/',user_views.register,name='register'),
     path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
     path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
     path('',include('home.urls')),
     path('index.html',home_views.home,name='index'),
     path('wands.html',wand_views.wands,name='wands'),
     path('brooms.html',include('brooms.urls')),
     path('books.html',include('books.urls')),
     path('orders.html',orders_views.orders,name='orders'),
     path('phoenix.html',wand_views.phoenix,name='phoenix'),
     path('thestral.html',wand_views.thestral,name='thestral'),
     path('elder.html',wand_views.elder,name='elder'),
     path('transfig.html',book_views.transfig,name='transfig'),
     path('dada.html',book_views.dada,name='dada'),
     path('potions.html',book_views.potions,name='potions'),
     path('nimbus.html',brooms_views.nimbus,name='nimbus'),
     path('normal.html',brooms_views.normal,name='normal'),
     path('firebolt.html',brooms_views.firebolt,name='firebolt')
]

