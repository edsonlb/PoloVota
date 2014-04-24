from django.conf.urls import patterns, include, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'listar'),
    url(r'^edit/$', 'editar'),
    url(r'^new/$', 'novo'),
    url(r'^delete/$', 'excluir'),
    url(r'^search/$', 'pesquisar'),
)