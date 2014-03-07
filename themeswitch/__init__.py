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
    (theme, '//netdna.bootstrapcdn.com/bootswatch/3.0.0/%s/bootstrap.min.css' % theme)
    for theme in BOOTSWATCHES
)

THEMES = dict(
    BOOTSWATCH_THEMES,
)
