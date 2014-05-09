# coding: utf-8
from django.contrib import admin
from projects.models import Projeto
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime #buscar quem foi cadastrado "hoje"
# Register your models here.

class ProjetoAdmin(admin.ModelAdmin):
	
	list_display = ('tema', 'projeto',
					'nomeOrientador','nomeIntegrante',
					 'redeSocial','modelagem','nomeLider',
					 'emailLider','telefoneLider','cpfLider', 'created_at','etapa')

	date_hierarchy = 'created_at' #necessário instalar o pytz (sudo pip isntall pytz)
	search_fields = ('tema','nomeOrientador', 'emailLider','telefoneLider', 'created_at')
	list_filter = ['created_at']

	def subscribed_today(self, obj): #obj recebe o obj da linha que está percorrendo
		return obj.created_at.date() == datetime.today().date() #buscar quem foi cadastrado "hoje"
	
	subscribed_today.short_description = _(u'Inscrito Hoje?')
	subscribed_today.boolean = True

admin.site.register(Projeto, ProjetoAdmin)