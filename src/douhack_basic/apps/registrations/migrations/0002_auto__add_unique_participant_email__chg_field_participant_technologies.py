# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Participant', fields ['email']
        db.create_unique(u'registrations_participant', ['email'])


        # Changing field 'Participant.technologies'
        db.alter_column(u'registrations_participant', 'technologies', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

    def backwards(self, orm):
        # Removing unique constraint on 'Participant', fields ['email']
        db.delete_unique(u'registrations_participant', ['email'])


        # Changing field 'Participant.technologies'
        db.alter_column(u'registrations_participant', 'technologies', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    models = {
        u'registrations.participant': {
            'Meta': {'ordering': "['-updated', '-created']", 'object_name': 'Participant'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'confirmation_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'technologies': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['registrations']