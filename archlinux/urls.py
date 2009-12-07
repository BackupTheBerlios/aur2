from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import aurprofile.views

from aur.feeds import RssLatestPackages, AtomLatestPackages

admin.autodiscover()

feeds_packages = {
    'rss': RssLatestPackages
    # 'atom': AtomLatestPackages,
}

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/register/$', 'registration.views.register',
        {'backend': 'registration.backends.default.DefaultBackend'}),
    (r'^accounts/login/$', 'aurprofile.views.remember_me_login',),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^profile/', include('aurprofile.urls')),
    (r'^', include('aur.urls')),
    (r'^openid/', include('django_openid_auth.urls')),
    (r'^feeds/(?P<url>.*)/packages/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds_packages}),
)

if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        })
    )
