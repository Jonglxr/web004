# core/signals.py
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def crear_grupos(sender, **kwargs):
    Producto = apps.get_model('catalog', 'Producto')
    permisos = Permission.objects.filter(content_type__app_label='catalog',
                                         content_type__model='producto')

    admin, _ = Group.objects.get_or_create(name='Administradores')
    vendedor, _ = Group.objects.get_or_create(name='Vendedores')

    if not admin.permissions.exists():
        admin.permissions.set(permisos)

    if not vendedor.permissions.exists():
        view_perm = permisos.get(codename='view_producto')
        vendedor.permissions.add(view_perm)