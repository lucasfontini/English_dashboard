from django.contrib import admin
from django.urls import path , include
from . import views
from rest_framework import routers

#aqui se define as rotas para que o django rest crie a estrutura
router = routers.DefaultRouter()
router.register('expressoes', views.api_expressoes, basename='get_expressoes')



urlpatterns = [
    path('', views.index, name='index'),
    path('adiciona/', views.addiciona_dados.as_view() , name='addiciona_dados'),
    path('galeria/<int:foto_id>', views.galeria , name='galeria'),
    path('editar/', views.editar, name='editar'),
    path('cadastra_dados/', views.Cadastra_dados , name='Cadastra_dados'),
    path('buscar/', views.buscar , name='buscar'),
    # aqui se importa a rota criada pelo django rest
    path('api/expressoes/', include(router.urls)),
    path('api/usuario/<int:pk>/expressoes/', views.ListaExpressoesPerUser.as_view()),
    



    
]


