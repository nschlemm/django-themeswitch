from django.template.base import Library

from themeswitch import THEMES

register = Library()

@register.simple_tag(takes_context=True)
def render_selected_theme_css(context):
    selected_theme = context['selected_theme']
    if selected_theme and selected_theme in THEMES:
        return u'<link href="%s" rel="stylesheet">' % THEMES[selected_theme]

    return u''


@register.assignment_tag()
def get_available_themes():
    available_themes = THEMES.keys()
    available_themes.sort()
    return available_themes
