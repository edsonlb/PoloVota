# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tema', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('universidade', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('universidadeOrientador', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('liderNome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('liderTelefone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('liderEmail', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('liderSocial', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('liderIntegrantes', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('link_slides', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('link_monografia', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('link_modelagem', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('link_website', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('link_outros', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('link_versionamento', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('etapa', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('ativo', self.gf('django.db.models.fields.CharField')(default='VAL', max_length=3)),
            ('dataAlteracao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('dataCadastro', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'projects_project')


    models = {
        u'projects.project': {
            'Meta': {'ordering': "['dataCadastro']", 'object_name': 'Project'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ativo': ('django.db.models.fields.CharField', [], {'default': "'VAL'", 'max_length': '3'}),
            'dataAlteracao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'dataCadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'etapa': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liderEmail': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'liderIntegrantes': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'liderNome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'liderSocial': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'liderTelefone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'link_modelagem': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'link_monografia': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'link_outros': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'link_slides': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'link_versionamento': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'link_website': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'tema': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'universidade': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'universidadeOrientador': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']