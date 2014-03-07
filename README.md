# django-themeswitch

_django-themeswitch_ is a django app that allows users to easily switch between a set of predefined stylings.

## Usage

To use _django-themeswitch_ update your `settings.py`:

- add `themeswitch` to your `INSTALLED_APPS`
- add 'themeswitch.context_processors.selected_theme' to your `TEMPLATE_CONTEXT_PROCESSORS`

Then add an entry in your `urls.py` to include `themeswitch.urls`.

In your templates after you `{% load themeswitch_tags %}` you have access to the template tags `{% get_available_themes as VARIABLENAME %}`
and `{% render_selected_theme_css %}`. Place the `{% render_selected_theme_css %}` somewhere in your template's `<head>`.

Now add an entry `THEMESWITCHER_THEMES` to your `settings.py`. `THEMESWITCHER_THEMES` should be a dictionary that contains mappings of `<theme_name>: <URL>`.
The URLs must be absolute, but can exclude the host. Example:

```python
THEMESWITCHER_THEMES = {
    'green': '/static/green.css'
}
```

This would make `get_available_themes` return just one theme, named 'green'.

Check out the [examples subdirectory](https://github.com/nschlemm/django-themeswitch/tree/master/examples).

# License

Copyright (c) 2013-2014, Nikolaus Schlemm
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or
other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
