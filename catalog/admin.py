from django.contrib import admin
from .models import Category, Artist, Artwork

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created', 'updated')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('created',)
    ordering = ('name',)

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'artist', 'featured', 'created')
    list_filter = ('category', 'artist', 'featured', 'created')
    search_fields = ('title', 'description')
    date_hierarchy = 'created'
    # Si prefieres ver un select con todas las opciones (en lugar de un campo de autocompletado
    # que requiere escribir para buscar), comenta/elimna la línea de abajo. Hecho así se mostrará
    # la lista completa de categorías y artistas en el formulario de creación/edición.
    # autocomplete_fields = ('category', 'artist')
    list_editable = ('featured',)
    ordering = ('-created',)

