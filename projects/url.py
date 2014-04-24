from django.conf.urls import patterns, include, url

urlpatterns = patterns('projects.views',
    url(r'^new/$', 'novo'),
    url(r'^edit/$', 'editar'),
    url(r'^search/$', 'pesquisar'),
    url(r'^delete/$', 'excluir'),
    url(r'^$', 'listar'),
)