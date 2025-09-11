from django.shortcuts import render
from django.http import HttpResponse
from financas.forms import RendaMensalForm
from financas.models import RendaMensal


# Create your views here.
def renda_view(request):
    if request.method == "POST":
        form = RendaMensalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("renda_view")  # redireciona para evitar reenvio
    else:
        form = RendaMensalForm()
python -m venv .env
    financas = RendaMensal.objects.all()
    return render(request, "financas/index.html", {"form": form, "financas": financas})
