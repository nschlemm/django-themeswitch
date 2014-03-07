from django.conf import settings
from django.http import HttpResponseBadRequest, HttpResponseRedirect



def switch(request):
    if 'theme' not in request.GET:
        return HttpResponseBadRequest('No theme defined')

    theme = request.GET.get('theme')
    if theme and theme not in settings.THEMESWITCHER_THEMES:
        return HttpResponseBadRequest('Unknown theme: "%s"' % theme)

    response = HttpResponseRedirect(
        request.GET.get('next', request.META.get('HTTP_REFERER', '/'),))
    if theme:
        response.set_cookie('selected_theme', theme)
    else:
        response.delete_cookie('selected_theme')
    return response
