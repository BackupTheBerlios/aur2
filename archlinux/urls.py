from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import aurprofile.forms
import aurprofile.views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/register/$', 'registration.views.register',
        {'backend': 'registration.backends.default.DefaultBackend',
            'form_class': aurprofile.forms.AurRegistrationForm } ),
    (r'^accounts/login/$', 'aurprofile.views.remember_me_login',
        {'form_class': aurprofile.forms.AuthenticationRememberMeForm } ),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^profile/', include('aurprofile.urls')),
    (r'^', include('aur.urls')),
    (r'^openid/', include('django_openid_auth.urls')),
)

if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        })
    )
