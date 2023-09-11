from django.contrib import admin
from django.urls import path, include
from usuarios.views import logout , login , cadastro, UserList


urlpatterns = [
    path('logout/',  logout, name = 'logout'),
    path('login/',  login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('api/users/', UserList.as_view()),

]
