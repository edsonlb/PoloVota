# coding: utf-8
from django.contrib import admin
from projects.models import Project
from django.utils.translation import ugettext as _
from django.utils.datetime_safe import datetime #buscar quem foi cadastrado "hoje"
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)