from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import aur.forms

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/register', 'registration.views.register', { 'form_class' :
        aur.forms.AurRegistrationForm } ),
    (r'^accounts/', include('registration.urls')),
    (r'^profile/', include('aurprofile.urls')),
    (r'^', include('aur.urls')),
)

if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        })
    )
