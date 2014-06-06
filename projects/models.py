# This Python file uses the following encoding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Project(models.Model):
    area = models.CharField(_('área'), max_length=100, blank=False, null=False)
    tema = models.CharField(_('tema'), max_length=200, blank=False, null=False)
    descricao = models.CharField(_('descrição'), max_length=400, blank=False, null=False)
    universidade = models.CharField(_('universidade'), max_length=200, null=False)
    universidadeOrientador = models.CharField(_('orientador'), max_length=200, blank=True, null=True)
    
    liderNome = models.CharField(_('líder'), max_length=200, null=False, blank=False)
    liderTelefone = models.CharField(_('telefone'), max_length=20, blank=False, null=False)
    liderEmail = models.EmailField(_('email'), max_length=100, null=False, blank=False)
    liderSocial = models.CharField(_('rede social'), max_length=200, blank=True)
    liderIntegrantes = models.CharField(_('integrantes'), max_length=400, blank=True, null=True)
    
    link_slides = models.CharField(_('slides'),  max_length=300, blank=True)
    link_monografia = models.CharField(_('monografia'),  max_length=300, blank=True)
    link_modelagem = models.CharField(_('modelagem'),  max_length=300, blank=True)
    link_website = models.CharField(_('website'),  max_length=300, blank=True)
    link_outros = models.CharField(_('outros'),  max_length=300, blank=True)
    link_versionamento = models.CharField(_('versionamento'),  max_length=300, blank=True)

    etapa = models.CharField(_('etapa'), max_length=3, blank=True)
    tags = models.CharField(_('tags'), max_length=300, blank=True)
    ativo = models.CharField(_('ativo'), max_length=3, default='VAL')
    
    dataAlteracao = models.DateTimeField(_('data de alteracao'), auto_now=True, auto_now_add=True)
    dataCadastro = models.DateTimeField(_('data de cadastro'), auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['dataCadastro']
        verbose_name = _(u'projeto')
        verbose_name_plural = _(u'projetos')

    def __unicode__(self):
        return self.tema +' - '+ self.liderNome

    def save(self, force_insert=False, force_update=False):
        self.area = self.area.upper()
        self.tema = self.tema.upper()
        self.descricao = self.descricao.upper()
        self.universidade = self.universidade.upper()
        self.universidadeOrientador = self.universidadeOrientador.upper()
        self.liderNome = self.liderNome.upper()
        self.liderEmail = self.liderEmail.upper()
        self.liderIntegrantes = self.liderIntegrantes.upper()
        self.etapa = self.etapa.upper()
        self.tags = self.tags.upper()
        self.ativo = self.ativo.upper()

        super(Project, self).save(force_insert, force_update)