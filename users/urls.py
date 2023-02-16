from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage, name='loginpage'),
    path('logout/', views.logoutpage, name='logoutpage'),

]