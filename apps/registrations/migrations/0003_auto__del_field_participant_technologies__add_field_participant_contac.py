# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Participant.technologies'
        db.delete_column(u'registrations_participant', 'technologies')

        # Adding field 'Participant.contacts'
        db.add_column(u'registrations_participant', 'contacts',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Participant.need_apartments'
        db.add_column(u'registrations_participant', 'need_apartments',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Participant.need_railway_station'
        db.add_column(u'registrations_participant', 'need_railway_station',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Participant.how_got_info'
        db.add_column(u'registrations_participant', 'how_got_info',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Participant.technologies'
        db.add_column(u'registrations_participant', 'technologies',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Deleting field 'Participant.contacts'
        db.delete_column(u'registrations_participant', 'contacts')

        # Deleting field 'Participant.need_apartments'
        db.delete_column(u'registrations_participant', 'need_apartments')

        # Deleting field 'Participant.need_railway_station'
        db.delete_column(u'registrations_participant', 'need_railway_station')

        # Deleting field 'Participant.how_got_info'
        db.delete_column(u'registrations_participant', 'how_got_info')


    models = {
        u'registrations.participant': {
            'Meta': {'ordering': "['-updated', '-created']", 'object_name': 'Participant'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'confirmation_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'how_got_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'need_apartments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_railway_station': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['registrations']