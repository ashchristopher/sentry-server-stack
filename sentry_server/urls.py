from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^sentry/', include('sentry.urls')),
    url(r'^media-server/(?P<path>.*)$', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }, name='media'),
)
