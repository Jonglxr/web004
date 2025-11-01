from django.shortcuts import render
from catalog.models import Artwork

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def faq(request):
    return render(request, 'core/faq.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def home(request):
    destacados = Artwork.objects.filter(featured=True).order_by('-created')[:8]
    noticias = [
        "Nueva exhibición de Shonen esta semana.",
        "Convocatoria de artistas abierta.",
        "Actualización del catálogo con obras clásicas.",
    ]
    return render(request, 'core/home.html', {'destacados': destacados, 'noticias': noticias})
