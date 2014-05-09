from django.db import models
from django.utils.translation import ugettext_lazy as _

class Projeto(models.Model):
	tema = models.CharField(_('tema'), max_length=300)
	projeto = models.CharField(_('projeto'), max_length=300)
	nomeOrientador = models.CharField(_('orientador'), max_length=100)
	nomeIntegrante = models.CharField(_('integrante'), max_length=200)
	redeSocial = models.CharField(_('rede social'), max_length=120, blank=True)
	modelagem = models.CharField(_('modelagem'),  max_length=20, blank=True)
	nomeLider = models.CharField(_('lider'), max_length=100)
	emailLider = models.EmailField(_('email'), unique=True)
	telefoneLider = models.CharField(_('telefone'), max_length=20, blank=True)
	cpfLider = models.CharField(_('cpf'), max_length=11, unique=True)
	created_at = models.DateTimeField(_('criado em'), auto_now_add=True)
	etapa = models.CharField(_('etapa'), max_length=3)
	tags = models.CharField(_('tags'), max_length=300)
	universidade = models.CharField(_('universidade'), max_length=100)

	class Meta:
		ordering = ['created_at']
		verbose_name = _(u'projeto')
		verbose_name_plural = _(u'projetos')

	def __unicode__(self):
		return self.tema + self.