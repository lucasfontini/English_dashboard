from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('chat/', views.chat , name='chat'),
    path('chat/req/', views.req , name='req'),
]