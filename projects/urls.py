from django.conf.urls import patterns, include, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'listar', name='listar'),
    url(r'^edit/$', 'editar', name='edit'),
    url(r'^new/$', 'novo', name='new'),
    url(r'^delete/$', 'excluir', name='delete'),
    url(r'^search/$', 'pesquisar', name='search'),
    url(r'^(\d+)/$', 'detail', name='detail'),
)