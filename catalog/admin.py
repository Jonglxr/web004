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
    autocomplete_fields = ('category', 'artist')
    list_editable = ('featured',)
    ordering = ('-created',)

