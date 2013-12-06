# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Company.name'
        db.alter_column(u'tcf14_company', 'name', self.gf('django.db.models.fields.CharField')(max_length=40))

    def backwards(self, orm):

        # Changing field 'Company.name'
        db.alter_column(u'tcf14_company', 'name', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'tcf14.booth': {
            'Meta': {'object_name': 'Booth'},
            'col': ('django.db.models.fields.IntegerField', [], {}),
            'filler': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.IntegerField', [], {})
        },
        u'tcf14.company': {
            'Meta': {'object_name': 'Company'},
            'booth': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tcf14.Booth']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tcf14']