from django.conf.urls import patterns, include, url

urlpatterns = patterns('persons.views',
    url(r'^vote/$', 'efetuarVoto'),
    url(r'^edit/$', 'editar'),
    url(r'^search/$', 'pesquisar'),
    url(r'^delete/$', 'excluir'),
    url(r'^$', 'listar'),
)