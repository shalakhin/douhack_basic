from django.conf.urls import patterns
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url('contacts/$', 'core.views.contacts', name='contacts'),
    # url(r'^douhack_basic/', include('douhack_basic.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^register/', 'core.views.register', name='register'),
    url(r'^confirm/(?P<id>\d+)/(?P<code>.+)/$',
        'core.views.confirm_registration',
        name='confirm'),
    url('^pages/', include('django.contrib.flatpages.urls')),
)

# if settings.DEBUG:
urlpatterns += patterns(
    '',
    url(r'^m/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^s/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)
