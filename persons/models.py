#coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import ugettext_lazy as _
from projects.models import Project


class Person(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # password
    # is_staff
    # is_active
    # is_superuser
    # last_login
    # date_joined
    empresa = models.CharField(
        _('empresa'), db_index=True, max_length='200', blank=False, null=False)

    class Meta:
        ordering = ['first_name']
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __unicode__(self):
        return unicode(self.email + ' (' + self.empresa + ')')

class PersonVote(models.Model):
    nota = models.IntegerField(_('nota'), db_index=True, blank=False, null=True, default=1)
    etapa = models.CharField(_('etapa'), max_length=3, blank=True)
    tags = models.CharField(_('tags'), max_length=300, blank=True)
    person = models.ForeignKey(Person)
    project = models.ForeignKey(Project)
    dataCadastro = models.DateTimeField(_('data de cadastro'), auto_now=False, auto_now_add=True, null=True)

    def __unicode__(self):
        return self.project.tema +' - '+ self.person.username

    def avg():
        return self.avg
