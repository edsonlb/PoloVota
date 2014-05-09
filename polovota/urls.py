from django.conf.urls import patterns, include, url
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.index'),
    url(r'^projects/', include('projects.urls')),
    url(r'^persons/', include('persons.urls')),
)