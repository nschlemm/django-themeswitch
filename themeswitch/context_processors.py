from django.conf import settings


def selected_theme(request):
    if request.COOKIES.get('selected_theme', None) in settings.THEMESWITCHER_THEMES:
        return {'selected_theme': request.COOKIES['selected_theme']}

    return {'selected_theme': None}
