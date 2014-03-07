# django-themeswitch

_django-themeswitch_ is a django app that allows users to easily switch between a set of predefined stylings.

## Usage

To use _django-themeswitch_ update your `settings.py`:

- add `themeswitch` to your `INSTALLED_APPS`
- add 'themeswitch.context_processors.selected_theme' to your `TEMPLATE_CONTEXT_PROCESSORS`

Then add an entry in your `urls.py` to include `themeswitch.urls`.

In your templates after you `{% load themeswitch_tags %}` you have access to the template tags `{% get_available_themes as VARIABLENAME %}`
and `{% render_selected_theme_css %}`. Place the `{% render_selected_theme_css %}` somewhere in your template's `<head>`.

Check out the examples subdirectory for a very simple project that shows how to use _django-themeswitch_.