from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sdms.views.index'),
    url(r'^sdms/', include('sample.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #url(r'^accounts/auth/$', 'sdms.views.auth_view'),
    url(r'^accounts/logout/$', 'sdms.views.logout'),
    url(r'^accounts/loggedin/$', 'sdms.views.loggedin'),
    url(r'^accounts/register/$', 'sdms.views.register_user'),
    url(r'^accounts/register_success/$', 'sdms.views.register_success'),
)
