from django.shortcuts import render

# Create your views here.

def helloworld(request):
    versao = "Versão 0.00 de 19/02/2022 8:00"
    return render(request, 'abolt.html', {'data':versao})
    
