from django.conf.urls import patterns, include, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'listar'),
    url(r'^login/$', 'login'),
    url(r'^save/$', 'salvar'),
    url(r'^new/$', 'novo'),
    url(r'^ranking/$', 'ranking'),
    url(r'^search/$', 'pesquisar'),
    url(r'^view/(?P<numero>\d+)/$', 'mostrar'),
    url(r'^validation/(?P<numero>\d+)/$', 'validation_ativo'),
    url(r'^prazos/$', 'prazos'),
)