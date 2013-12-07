# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'tcf14_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
        ))
        db.send_create_signal(u'tcf14', ['User'])

        # Adding model 'Visit'
        db.create_table(u'tcf14_visit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tcf14.Company'])),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tcf14.User'], null=True, blank=True)),
        ))
        db.send_create_signal(u'tcf14', ['Visit'])

        # Adding model 'Checkin'
        db.create_table(u'tcf14_checkin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tcf14.Company'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tcf14.User'])),
        ))
        db.send_create_signal(u'tcf14', ['Checkin'])


        # Changing field 'Company.description'
        db.alter_column(u'tcf14_company', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'tcf14_user')

        # Deleting model 'Visit'
        db.delete_table(u'tcf14_visit')

        # Deleting model 'Checkin'
        db.delete_table(u'tcf14_checkin')


        # Changing field 'Company.description'
        db.alter_column(u'tcf14_company', 'description', self.gf('django.db.models.fields.TextField')(default='N/A'))

    models = {
        u'tcf14.booth': {
            'Meta': {'object_name': 'Booth'},
            'col': ('django.db.models.fields.IntegerField', [], {}),
            'filler': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.IntegerField', [], {})
        },
        u'tcf14.checkin': {
            'Meta': {'object_name': 'Checkin'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tcf14.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tcf14.User']"})
        },
        u'tcf14.company': {
            'Meta': {'object_name': 'Company'},
            'booth': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tcf14.Booth']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'tcf14.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'tcf14.visit': {
            'Meta': {'object_name': 'Visit'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tcf14.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tcf14.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['tcf14']