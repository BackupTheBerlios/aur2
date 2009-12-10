from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import aurprofile.forms
import aurprofile.views
from django.contrib.auth.models import User
from aur.feeds import RssLatestPackages, AtomLatestPackages

admin.autodiscover()

feeds_packages = {
    'rss': RssLatestPackages
    # 'atom': AtomLatestPackages,
}

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/register/$', 'registration.views.register',
        {'backend': 'aur.forms.AddGroupDefaultBackend',
            'form_class': aurprofile.forms.AurRegistrationForm } ),
    (r'^accounts/login/$', 'aurprofile.views.remember_me_login',),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^profile/', include('aurprofile.urls')),
    (r'^', include('aur.urls')),
    (r'^openid/', include('django_openid_auth.urls')),
    (r'^feeds/(?P<url>.*)/packages/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds_packages}),
    (r'^users/(?P<user>\w+)/packages', 'aur.views.user_packages'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
)

if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        })
    )
