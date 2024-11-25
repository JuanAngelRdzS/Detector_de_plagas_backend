from django.shortcuts import render, redirect
from .models import Registro
from .models import Plaga  # Asegúrate de que esto esté presente

# Create your views here.

def home(request):
    reg = Registro.objects.all()
    return render(request, "gestionUsers.html", {"registro": reg})

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

# Vista para registrar una nueva plaga
def registrarPlaga(request):
    IdPlaga=request.POST['numidplaga']
    NamePlaga=request.POST['txtplaga']
    DescPlaga=request.POST['txtdesc']

    plaga = Plaga.objects.create(
        IdPlaga=IdPlaga, NamePlaga=NamePlaga, DescPlaga=DescPlaga
    )
    return redirect('/')

def editarPlaga(request, IdPlaga):
    plaga = Plaga.objects.get(IdPlaga=IdPlaga)
    return render(request, "editarPlaga.html", {"plaga": plaga})

def editaPlaga(request, IdPlaga):
    IdPlaga=request.POST['numidplaga']
    NamePlaga = request.POST['txtplaga']
    DescPlaga = request.POST['txtdesc']

    plaga = Plaga.objects.get(IdPlaga=IdPlaga)
    plaga.NamePlaga = NamePlaga
    plaga.DescPlaga = DescPlaga
    plaga.save()

    return redirect('/')

def borrarPlaga(request, IdPlaga):
     plaga = Plaga.objects.get(IdPlaga=IdPlaga)
     plaga.delete()

     return redirect('/')