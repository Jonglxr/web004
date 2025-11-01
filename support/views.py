from django.shortcuts import render
from .forms import ContactForm

def contacto(request):
    form = ContactForm()
    return render(request, 'support/contacto.html', {'form': form})
