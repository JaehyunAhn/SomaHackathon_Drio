from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import os.path
admin.autodiscover()

site_media = os.path.join(
        os.path.dirname(__file__),'site_media'
)


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'MatchingSys.views.main_page'),
    url(r'^loggedon/$', 'MatchingSys.views.loggedon'),
    url(r'^logout/$', 'MatchingSys.views.logout_user'),
    url(r'^register/$', 'MatchingSys.views.register_user'),
    url(r'^messagebox/','MatchingSys.views.messageBox'),
        
    url(r'^avatar/', include('avatar.urls')),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',
        { 'document_root':site_media,}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,}),
)
