# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Company.booth'
        db.alter_column(u'tcf14_company', 'booth_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tcf14.Booth'], unique=True, null=True))

        # Changing field 'Company.logo'
        db.alter_column(u'tcf14_company', 'logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Company.booth'
        raise RuntimeError("Cannot reverse this migration. 'Company.booth' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Company.booth'
        db.alter_column(u'tcf14_company', 'booth_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tcf14.Booth'], unique=True))

        # User chose to not deal with backwards NULL issues for 'Company.logo'
        raise RuntimeError("Cannot reverse this migration. 'Company.logo' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Company.logo'
        db.alter_column(u'tcf14_company', 'logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'tcf14.booth': {
            'Meta': {'object_name': 'Booth'},
            'col': ('django.db.models.fields.IntegerField', [], {}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tcf14']