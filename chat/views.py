from django.shortcuts import render
from .get_chat import handle_message
# Create your views here.

def chat(request):
    context = {'message': "oi"}
    return render(request, 'index1.html', context)
 
def req(request):
    print(request.POST)
    if request.method == 'POST':
        pergunta = request.POST.get('chatinput')        
        resposta = handle_message(pergunta)
        print(resposta)
        context = {'message': resposta}
        return render(request, 'index1.html', context)
    else:
        return render(request, 'index1.html')