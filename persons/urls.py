from django.conf.urls import patterns, include, url


urlpatterns = patterns('persons.views',
	url(r'^login/$', 'loginRedirect'),
	url(r'^dologin/$', 'login'),
	url(r'^$', 'listar'),
    #url(r'^vote/$', 'efetuarVoto'),
    url(r'^edit/(?P<pk>\d+)/$', 'editar'),
    url(r'^save/$', 'adicionar'),
    #url(r'^search/$', 'pesquisar'),
    #url(r'^delete/$', 'excluir'),
    
)
