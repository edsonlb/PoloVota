from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import ugettext_lazy as _


class Person(AbstractUser):
    #user = models.OneToOneField('auth.User')
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
        _('Empresa'), db_index=True, max_length='200', blank=False, null=False)

    class Meta:
        ordering = ['first_name']
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __unicode__(self):
        return unicode(self.first_name + ' (' + self.empresa + ')')
