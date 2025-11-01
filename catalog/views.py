from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Artwork, Category, Artist

def gallery_list(request):
    qs = Artwork.objects.all().order_by('-created')

    category_slug = request.GET.get('categoria')
    artist_id = request.GET.get('artista')

    if category_slug:
        qs = qs.filter(category__slug=category_slug)
    if artist_id:
        qs = qs.filter(artist_id=artist_id)

    paginator = Paginator(qs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all().order_by('name')
    artists = Artist.objects.all().order_by('name')

    return render(request, 'catalog/gallery_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'artists': artists,
        'active_category': category_slug,
        'active_artist': artist_id,
    })

def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'catalog/artwork_detail.html', {'artwork': artwork})
