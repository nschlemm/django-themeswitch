from django.core.exceptions import ImproperlyConfigured

from .settings import DEFAULT_THEME, THEMES


def selected_theme(request):
    theme = request.COOKIES.get('selected_theme', DEFAULT_THEME)
    if theme not in THEMES:
        theme = DEFAULT_THEME

    return {'selected_theme': theme}
