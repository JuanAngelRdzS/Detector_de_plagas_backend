from django.shortcuts import render, redirect
from .models import Registro
from .models import Plaga  # Asegúrate de que esto esté presente
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.middleware.csrf import get_token
import cv2
import numpy as np
from ultralytics import YOLO
from django.http import JsonResponse
from django.core.files.storage import default_storage
from PIL import Image
import os


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
 
def load_model():
    model_path = 'aplicaciones/hojita/best.pt'
    model = YOLO(model_path)  # Cargar el modelo
    return model

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Ruta de la imagen que deseas analizar (puedes cambiarla a una imagen de prueba)
        image_file = request.FILES['image']
        
        upload_dir = os.path.join('media/uploads')

        # Verificar si la imagen existe
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # Guardar el archivo
        file_path = default_storage.save(f'uploads/{image_file.name}', image_file)
        
        # Obtener la ruta completa del archivo guardado
        full_file_path = os.path.join(f'media/uploads/{image_file.name}')
        
        # Cargar el modelo y leer la imagen
        model = load_model()
        img = cv2.imread(full_file_path)  # Asegúrate de que full_file_path esté correcto

        if img is None:
            return JsonResponse({'error': 'Failed to load image'}, status=500)

        # Realizar el análisis
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB
        img = cv2.resize(img, (640, 640))  # Redimensionar a 640x640
        
        # Realizar la detección con el modelo
        results = model(img)
        prediction = results[0]

        if len(prediction.boxes.cls) == 0:
            return JsonResponse({'message': 'No detections made'}, status=200)

        # Extraer las predicciones
        pred_classes = prediction.names
        pred_labels = prediction.boxes.cls
        pred_confidences = prediction.boxes.conf

        predictions = []
        for label, confidence in zip(pred_labels, pred_confidences):
            predictions.append({
                'class': pred_classes[int(label)],
                'confidence': float(confidence)
            })

        return JsonResponse({
            'message': 'Image processed successfully',
            'file_path': file_path,
            'predictions': predictions
        })

    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

def csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})

# def upload_image(request):
#     if request.method == 'POST':
#         image_file = '/media/uploads/ej1.1.jpg'
        
#         # Verificar si la imagen existe
#         if not os.path.exists(image_file):
#             return JsonResponse({'error': 'Test image not found'}, status=404)

#         # Leer la imagen desde el archivo local
#         img = cv2.imread(image_file)

#         if img is None:
#             return JsonResponse({'error': 'Failed to load image'}, status=500)

#         # Cargar el modelo
#         model = load_model()

#         # Realizar el análisis
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB
#         img = cv2.resize(img, (640, 640))  # Redimensionar a 640x640

#         # Realizar la detección con el modelo
#         results = model(img)
#         prediction = results[0]

#         if len(prediction.boxes.cls) == 0:
#             return JsonResponse({'message': 'No detections made'}, status=200)

#         # Extraer las predicciones
#         pred_classes = prediction.names
#         pred_labels = prediction.boxes.cls
#         pred_confidences = prediction.boxes.conf

#         predictions = []
#         for label, confidence in zip(pred_labels, pred_confidences):
#             predictions.append({
#                 'class': pred_classes[int(label)],
#                 'confidence': float(confidence)
#             })

#         return JsonResponse({
#             'message': 'Image processed successfully',
#             'predictions': predictions
#         })

#     else:
#         return JsonResponse({'error': 'Invalid request'}, status=400)