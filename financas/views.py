from django.shortcuts import render
from django.http import HttpResponse
from financas.forms import RendaMensalForm
from financas.models import RendaMensal


# Create your views here.
def Exibicacao(request):

    if request.method == 'GET':
        financas = RendaMensal.objects.all()
        context = {
            'RendaMensal': RendaMensal,
            'form': RendaMensalForm
        }
        return render(request,'principal/index.html',context)
    
    if request.method == 'POST':
        form = RendaMensalForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'principal/index.html')
