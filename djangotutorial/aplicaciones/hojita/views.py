from django.shortcuts import render, redirect
from .models import Registro

# Create your views here.

def home(request):
    reg = Registro.objects.all()
    return render(request, "gestionUsers.html", {"registros": reg})

def registrarUsuario(request):
    IdUser=request.POST['numiduser']
    NameUser=request.POST['txtname']
    CorreoUse=request.POST['txtCorreo']

    registro = Registro.objects.create(
        IdUser=IdUser, NameUser=NameUser, CorreoUse=CorreoUse
    )
    return redirect('/')

def editarUser(request, IdUser):
    registro = Registro.objects.get(IdUser=IdUser)
    return render(request, "editarUser.html", {"registro": registro})

def editaUser(request, IdUser):
    NameUser = request.POST['txtname']
    CorreoUse = request.POST['txtCorreo']

    registro = Registro.objects.get(IdUser=IdUser)
    registro.NameUser = NameUser
    registro.CorreoUse = CorreoUse
    registro.save()

    return redirect('/')



def borrarUser(request, IdUser):
     registro = Registro.objects.get(IdUser=IdUser)
     registro.delete()

     return redirect('/')
