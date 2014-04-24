from django.conf.urls import patterns, include, url

urlpatterns = patterns('persons.views',
    url(r'^vote/$', 'efetuarVoto'),
    url(r'^edit/(?P<pk>\d+)/$', 'editar'),
    url(r'^save/$', 'salvar'),
    url(r'^search/$', 'pesquisar'),
    url(r'^delete/$', 'excluir'),
    url(r'^$', 'listar'),
)