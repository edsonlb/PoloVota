from django.conf.urls import patterns, include, url


urlpatterns = patterns('persons.views',
	url(r'^login/$', 'loginRedirect'),
	url(r'^logout/$', 'logoutRedirect'),
	url(r'^dologin/$', 'login'),
    url(r'^initial/$', 'loginInicial'),
    url(r'^voted/$', 'loginVoted'),
    url(r'^edit/(?P<pk>\d+)/$', 'editar'),
    url(r'^show/(?P<pk>\d+)/$', 'show'),    
    url(r'^save/$', 'adicionar'),
    url(r'^score/$', 'saveScore'),
    url(r'^ranking/$', 'ranking'),
    
)
