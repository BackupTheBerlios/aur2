from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('aurprofile.views',
    url(r'^(?P<object_id>\w+)$', 'user_details',
        name='aurprofile_profile'),
)
