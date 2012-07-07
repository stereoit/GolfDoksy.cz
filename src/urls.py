from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls')),
    url(r'^turnaje/', include('tournaments.urls')),
    url(r'^aktuality/$', 'news.views.news'),
    url(r'^hraci/', include('players.urls')),
    url(r'^galerie/$', 'news.views.gallery'),
    url(r'^galerie/(?P<slug>[a-zA-Z0-9_.-]*)/$', 'news.views.gallery'),
    url(r'^clean/$', direct_to_template,{'template':'clean.html'}, name="clean"),
    url(r'^xxx/$', direct_to_template,{'template':'login-bar.html'}, name="browserid"),
    url(r'^browserid/$', direct_to_template,{'template':'browserid.html'}, name="browserid"),
    url(r'^logged-in/$', direct_to_template,{'template':'logged_in.html'}, name="logged_in"),
#    url(r'^partner/(?P<slug>[-\w]+)/$', PartnerDetailView.as_view(), name="partner_detail"),
    url(r'^', include('social_auth.urls')),
    url(r'^', include('cms.urls')),
)


if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
    #url(r'^openid/', include('django_openid_auth.urls')),
) + urlpatterns + staticfiles_urlpatterns()
