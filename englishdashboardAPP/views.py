from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Expressao
from django.contrib import messages
from django.http import JsonResponse
from rest_framework import viewsets , generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import ExpressaoSerializer 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters






def index(request):

# define se usuario esta logado ou nao 
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')


    expressoes = Expressao.objects.all()
    context = {"dados": expressoes}
    return render(request, 'index.html', context)
# Create your views here.


class addiciona_dados(TemplateView):

    template_name = "Adiciona_data.html"


def Cadastra_dados(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    if request.method == 'POST':
        expression = request.POST.get('test')
        meaning = request.POST.get('meaning')
        Exemplo = request.POST.get('example')
        foto = request.POST.get('foto')
        insercao = Expressao(name=expression, meaning=meaning,
                             exemple=Exemplo, foto=foto)
        insercao.save()

    expressoes = Expressao.objects.all()
    context = {"dados": expressoes}
    return render(request, 'index.html', context)


def galeria(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    foto = get_object_or_404(Expressao, pk=foto_id)
    return render(request, 'galeria.html', {'fotos': foto})


def editar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    expressoes = Expressao.objects.all()
    context = {"dados":expressoes}
    return render(request, 'index.html', context)

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    if request.method == 'GET':
            item_a_buscar = request.GET['buscar']
            expressoes = Expressao.objects.filter(name=item_a_buscar)

            context = {"dados": expressoes}

    return render(request, 'buscar.html' , context)






#teste de api 

class api_expressoes(viewsets.ModelViewSet):
    "api que mostra as expressoes via rest"
    queryset = Expressao.objects.all()
    serializer_class = ExpressaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter ]
    

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', "exemple",]
    filterset_fields = ['usuario']

    # https://www.django-rest-framework.org/api-guide/filtering/

    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['name', ]
    # # ordering_fields = '__all__'

class ListaExpressoesPerUser(generics.ListAPIView):
    serializer_class = ExpressaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    """ lista as expressoes por user """
    def get_queryset(self):
        query_set = Expressao.objects.filter(usuario=self.kwargs['pk'])
        return query_set
    


# def api_expressoes(request):
#     if request.method == 'GET':
#         expressoes = Expressao.objects.all()
#         print(type(expressoes))
#         test = {'1':'test'}
#         print(expressoes)
#         return  JsonResponse(expressoes)