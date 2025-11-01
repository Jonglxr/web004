from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
    path('obra/<int:pk>/', views.artwork_detail, name='artwork_detail'),
]
