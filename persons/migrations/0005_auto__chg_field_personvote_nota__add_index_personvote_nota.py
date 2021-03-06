# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PersonVote.nota'
        db.alter_column(u'persons_personvote', 'nota', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Adding index on 'PersonVote', fields ['nota']
        db.create_index(u'persons_personvote', ['nota'])


    def backwards(self, orm):
        # Removing index on 'PersonVote', fields ['nota']
        db.delete_index(u'persons_personvote', ['nota'])


        # Changing field 'PersonVote.nota'
        db.alter_column(u'persons_personvote', 'nota', self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 7, 14, 0, 0), max_length=100))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'persons.person': {
            'Meta': {'ordering': "['first_name']", 'object_name': 'Person'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.CharField', [], {'max_length': "'200'", 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'persons.personvote': {
            'Meta': {'object_name': 'PersonVote'},
            'dataCadastro': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'etapa': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nota': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'db_index': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['persons.Person']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Project']"}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
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

    complete_apps = ['persons']