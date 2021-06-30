from django.shortcuts import render
from .models import Colaborador

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Colab(request):
    colaborador = Colaborador.objects.all()
    return render(request,'core/Colaboradores.html',{'colaborador':colaborador})