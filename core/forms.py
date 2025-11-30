from django import forms
from django.contrib.auth.models import User, Group, Permission
from django.apps import apps
from django.shortcuts import render
from django.core.mail import send_mail

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)


class RegistroAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = True

        if commit:
            user.save()
            grupo, creado = Group.objects.get_or_create(name='Administradores')

            if creado or not grupo.permissions.exists():
                modelos = ['artwork', 'category', 'artist']

                for modelo in modelos:
                    permisos = Permission.objects.filter(
                        content_type__app_label='catalog',
                        content_type__model=modelo
                    )
                    grupo.permissions.add(*permisos)

            user.groups.add(grupo)

        return user



class RegistroVendedorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = True

        if commit:
            user.save()

            grupo, creado = Group.objects.get_or_create(name='Vendedores')

            if creado or not grupo.permissions.exists():
                Articulo = apps.get_model('catalog', 'Articulo')
                view_perm = Permission.objects.get(
                    content_type__app_label='catalog',
                    content_type__model='articulo',
                    codename='view_articulo'
                )
                grupo.permissions.set([view_perm])

            user.groups.add(grupo)

        return user
