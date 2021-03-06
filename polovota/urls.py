from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'core.views.index'),
    url(r'^login/$', 'core.views.login'),
    url(r'^email/$', 'core.views.email'),
    url(r'^save/$', 'core.views.save'),
    url(r'^validation/$', 'core.views.validation'),
    url(r'^validation_error/$', 'core.views.validation_error'),
    url(r'^projects/', include('projects.urls')),
    url(r'^persons/', include('persons.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)