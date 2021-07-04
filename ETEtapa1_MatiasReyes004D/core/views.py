from django.shortcuts import render
from .models import Colaborador
from .forms import FormColab

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Colab(request):
    colaborador = Colaborador.objects.all()
    return render(request,'core/Colaboradores.html',{'colaborador':colaborador})

def agregar(request):
    if request.method == 'POST':
        agregar = FormColab(request.POST, request.FILES)
        if agregar.is_valid():
            agregar.save()
            return redirect('Colab')
    else:
        agregar = FormColab()
    return render(request,'core/form_cola.html',{'agregar':agregar})
def modificar(reques,id):
    comentario = Colaborador.objects.get(rut=id)
    datos ={
        'form': FormColab(instance=comentario)
    }
    if request.method =='POST':
        formu = FormColab(data=request.POST, instance = comentario)
        if formu.is_valid:
            formu.save()
            return redirect(Colab)
    return render(request,'core/modificar.html',datos)
def eliminar(request,id):
    comentario = Colaborador.objects.get(rut=id)
    comentario.delete()
    return redirect('Colab')