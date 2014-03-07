from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'', include('themeswitch.urls')),
    url(r'^$', 'bootswatch_example.views.home', name='home'),
)
