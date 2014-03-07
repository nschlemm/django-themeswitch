def _get_bootswatch_css_url(theme, bootstrap_version='3.0.0'):
    "little helper to generate a bootswatch theme's css url"
    css_url = '//netdna.bootstrapcdn.com/bootswatch/%s/%s/bootstrap.min.css'
    return css_url % (bootstrap_version, theme)


BOOTSWATCHES = (
    'amelia',
    'cerulean',
    'cosmo',
    'cyborg',
    'flatly',
    'journal',
    'readable',
    'simplex',
    'slate',
    'spacelab',
    'united',
)


BOOTSWATCH_THEMES = dict(
    (theme, _get_bootswatch_css_url(theme))
    for theme in BOOTSWATCHES
)

THEMES = dict(
    BOOTSWATCH_THEMES,
)
