from .settings import DEFAULT_THEME, THEMES


def selected_theme(request):
    if request.COOKIES.get('selected_theme', DEFAULT_THEME) in THEMES:
        return {'selected_theme': request.COOKIES['selected_theme']}

    return {'selected_theme': DEFAULT_THEME}
