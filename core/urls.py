from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quienes-somos/', views.about, name='about'),
    path('preguntas-frecuentes/', views.faq, name='faq'),
    path('registro/admin/', views.registrar_admin, name='registro_admin'),
    path('registro/vendedor/', views.registrar_vendedor, name='registro_vendedor'),
    path('contacto/', views.contacto, name='contacto'),

]
