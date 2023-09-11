from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User 
from rest_framework import generics
from .serializer import UserSerializer
#biblionte de login auth abaixo
from django.contrib import auth, messages

# Create your views here.




# É possível verificar em um template se o usuário está logado com o código {% if user.is_authenticated %}.


def login(request):
    form = LoginForm()
    context = {'form':form}

    if request.method == "POST":
        form = LoginForm(request.POST)

        
        if form.is_valid():
            name = form['nome_Login'].value()
            password = form['senha'].value()
            print(name, password)
        usuario = auth.authenticate(request, username=name, password=password)
        if usuario is not None:
            # envia o usuario para a auth do django 
            auth.login(request, usuario)
            messages.success(request, f'Usuario {usuario} autorizado')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')


    return render(request, "login.html" ,  context )

def cadastro(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        print(request.POST)
        if User.objects.filter(username=name).exists():
            return redirect('cadastro') 
        
        Usuario = User.objects.create_user(
            username=name,
            email=email, 
            password=password
        )
        Usuario.save()
        redirect ('login')





    else:
        # Handle requests with other methods (e.g. GET)
        pass

    return render(request, "cadastro.html")


def logout(request):
        auth.logout(request)
        messages.success(request, "Logout efetuado com sucesso!")
        return redirect('login')

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer