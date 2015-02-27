from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^enter/', 'sample.views.enter'),
    url(r'^success/', 'sample.views.success'),
    url(r'^search/', 'sample.views.search'),
    url(r'^range_search/', 'sample.views.range_search'),
    url(r'^update/(?P<id>\d+)/$', 'sample.views.update'),
    url(r'^delete/(?P<id>\d+)/$', 'sample.views.delete'),
)