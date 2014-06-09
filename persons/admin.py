# coding: utf-8
from django.contrib import admin
from persons.models import Person

class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)