# This Python file uses the following encoding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Project(models.Model):
    area = models.CharField(_('área'), max_length=100)
    tema = models.CharField(_('tema'), max_length=200)
    descricao = models.CharField(_('descrição'), max_length=400)
    universidade = models.CharField(_('universidade'), max_length=200)
    universidadeOrientador = models.CharField(_('orientador'), max_length=200)
    
    liderNome = models.CharField(_('líder'), max_length=200)
    liderTelefone = models.CharField(_('telefone'), max_length=20, blank=True)
    liderEmail = models.EmailField(_('email'), unique=True)
    liderSocial = models.CharField(_('rede social'), max_length=120, blank=True)
    liderIntegrantes = models.CharField(_('integrantes'), max_length=400)
    
    link_slides = models.CharField(_('slides'),  max_length=300, blank=True)
    link_monografia = models.CharField(_('monografia'),  max_length=300, blank=True)
    link_modelagem = models.CharField(_('modelagem'),  max_length=300, blank=True)
    link_website = models.CharField(_('website'),  max_length=300, blank=True)
    link_outros = models.CharField(_('outros'),  max_length=300, blank=True)
    link_versionamento = models.CharField(_('versionamento'),  max_length=300, blank=True)

    etapa = models.CharField(_('etapa'), max_length=3)
    tags = models.CharField(_('tags'), max_length=300)
    ativo = models.CharField(_('ativo'), max_length=300)
    
    dataAlteracao = models.DateTimeField(_('data de alteracao'), auto_now=True, auto_now_add=True)
    dataCadastro = models.DateTimeField(_('data de cadastro'), auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['dataCadastro']
        verbose_name = _(u'projeto')
        verbose_name_plural = _(u'projetos')

    def __unicode__(self):
        return self.tema +' - '+ self.liderNome