from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('aurprofile.views',
    url(r'^(?P<username>\w+)$', 'profile',
        name='aurprofile_profile'),
)
