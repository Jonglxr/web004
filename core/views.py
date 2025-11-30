from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from catalog.models import Artwork
from django.core.cache import cache
from django.conf import settings
from .forms import RegistroAdminForm, RegistroVendedorForm
from django.core.mail import send_mail
from .forms import ContactForm

def contacto(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            # Construir el mensaje
            asunto = f"Nuevo mensaje de contacto de {nombre}"
            cuerpo = f"Nombre: {nombre}\nEmail: {email}\n\nMensaje:\n{mensaje}"

            # Enviar a Mailtrap
            send_mail(
                asunto,
                cuerpo,
                email,  # remitente
                ["noreply@museodelanime.cl"],
                fail_silently=False,
            )

            return render(request, "support/contacto_exitoso.html")
    else:
        form = ContactForm()

    return render(request, "support/contacto.html", {"form": form})


@require_http_methods(["GET"])
def home(request):
    try:
        # Intentamos obtener los destacados del cache
        destacados = cache.get('destacados_home')
        if destacados is None:
            destacados = Artwork.objects.filter(featured=True).order_by('-created')[:8]
            # Guardamos en cache por 1 hora
            cache.set('destacados_home', destacados, 3600)

        noticias = [
            "Nueva exhibición de Shonen esta semana.",
            "Convocatoria de artistas abierta.",
            "Actualización del catálogo con obras clásicas.",
        ]
        context = {
            'destacados': destacados,
            'noticias': noticias,
            'section': 'home'
        }
        return render(request, 'core/home.html', context)
    except Exception as e:
        if settings.DEBUG:
            raise e
        return render(request, '500.html', status=500)

@require_http_methods(["GET"])
def about(request):
    try:
        context = {
            'section': 'about',
            'team_members': [
                {
                    'name': 'Ana García',
                    'role': 'Directora de Galería',
                    'bio': 'Experta en arte contemporáneo con más de 10 años de experiencia.'
                },
                {
                    'name': 'Carlos López',
                    'role': 'Curador Principal',
                    'bio': 'Especialista en arte digital y nuevos medios.'
                }
            ]
        }
        return render(request, 'core/about.html', context)
    except Exception as e:
        if settings.DEBUG:
            raise e
        return render(request, '500.html', status=500)

@require_http_methods(["GET"])
def faq(request):
    try:
        context = {
            'section': 'faq',
            'faqs': [
                {
                    'question': '¿Cómo puedo comprar una obra?',
                    'answer': 'Puede contactarnos directamente a través del formulario de contacto.'
                },
                {
                    'question': '¿Realizan envíos internacionales?',
                    'answer': 'Sí, trabajamos con servicios de envío especializados en obras de arte.'
                }
            ]
        }
        return render(request, 'core/faq.html', context)
    except Exception as e:
        if settings.DEBUG:
            raise e
        return render(request, '500.html', status=500)

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

def registrar_admin(request):
    form = RegistroAdminForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/admin/login/')
    return render(request, 'core/registro_admin.html', {'form': form})

def registrar_vendedor(request):
    form = RegistroVendedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/admin/login/')
    return render(request, 'core/registro_vendedor.html', {'form': form})
