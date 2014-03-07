from django.conf import settings

THEMES = getattr(settings, 'THEMESWITCHER_THEMES', dict())
