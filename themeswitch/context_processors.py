from themeswitch import THEMES


def selected_theme(request):
    if 'selected_theme' in request.COOKIES and \
            request.COOKIES['selected_theme'] in THEMES:
        return {'selected_theme': request.COOKIES['selected_theme']}

    return {'selected_theme': None}
