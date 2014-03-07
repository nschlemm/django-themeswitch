from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template.base import Library

register = Library()


@register.simple_tag(takes_context=True)
def render_selected_theme_css(context):
    if not 'selected_theme' in context:
        context_processor = 'themeswitch.context_processors.selected_theme'
        if context_processor not in settings.TEMPLATE_CONTEXT_PROCESSORS:
            raise ImproperlyConfigured(
                'Add %s to TEMPLATE_CONTEXT_PROCESSORS' % context_processor
            )
    selected_theme = context['selected_theme']
    if selected_theme and selected_theme in settings.THEMESWITCHER_THEMES:
        return u'<link href="%s" rel="stylesheet">' % settings.THEMESWITCHER_THEMES[selected_theme]

    return u''


@register.assignment_tag()
def get_available_themes():
    if 'THEMESWITCHER_THEMES' not in settings:
        raise ImproperlyConfigured('Please add themes via settings.THEMESWITCHER_THEMES')
    available_themes = settings.THEMESWITCHER_THEMES.keys()
    available_themes.sort()
    return available_themes
