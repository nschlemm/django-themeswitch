from themeswitch import THEMES


def selected_theme(request):
    if request.COOKIES.get('selected_theme', None) in THEMES:
        return {'selected_theme': request.COOKIES['selected_theme']}

    return {'selected_theme': None}
