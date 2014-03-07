from django.conf.urls import patterns, url

from .views import switch

urlpatterns = patterns('',
    url(r'^switch/$', switch, name='themeswitch-switch'),
)
