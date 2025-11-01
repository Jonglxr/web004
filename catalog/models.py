
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self): return self.name

class Artist(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self): return self.name

class Artwork(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='obras/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='artworks')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)

    def __str__(self): return self.title

