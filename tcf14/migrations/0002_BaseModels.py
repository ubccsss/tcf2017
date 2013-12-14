# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Booth'
        db.create_table(u'tcf14_booth', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('col', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'tcf14', ['Booth'])

        # Adding model 'Company'
        db.create_table(u'tcf14_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('booth', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tcf14.Booth'], unique=True)),
        ))
        db.send_create_signal(u'tcf14', ['Company'])


    def backwards(self, orm):
        # Deleting model 'Booth'
        db.delete_table(u'tcf14_booth')

        # Deleting model 'Company'
        db.delete_table(u'tcf14_company')


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
            'booth': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tcf14.Booth']", 'unique': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tcf14']