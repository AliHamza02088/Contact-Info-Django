from django.contrib import admin
from home import views
from django.urls import path,include

urlpatterns = [
    path('index/', views.index, name = "home"),
    path('', views.loginUser, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
]
