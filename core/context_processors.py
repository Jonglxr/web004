def site_settings(request):
    return {
        'SITE_NAME': 'Museo del Anime',
        'SITE_TWITTER': 'https://twitter.com/anime_museo',
        'SITE_INSTAGRAM': 'https://instagram.com/anime_museo',
        'SITE_THEME': 'dark',  # ejemplo de uso en templates
    }
