from django.conf import settings

DEFAULT_THEME = getattr(settings, 'THEMESWITCHER_DEFAULT_THEME', None)
THEMES = getattr(settings, 'THEMESWITCHER_THEMES', dict())
