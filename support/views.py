from django.shortcuts import render
from .forms import ContactForm

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def contacto(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            cuerpo = f"Nombre: {nombre}\nEmail: {email}\n\nMensaje:\n{mensaje}"

            send_mail(
                asunto,
                cuerpo,
                settings.DEFAULT_FROM_EMAIL,
                ["noreply@museodelanime.cl"],  # puede ser cualquiera, Mailtrap lo captura
                fail_silently=False,
            )

            return render(request, "support/contacto_exitoso.html")
    else:
        form = ContactForm()

    return render(request, "support/contacto.html", {"form": form})
