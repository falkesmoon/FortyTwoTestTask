# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bio'
        db.create_table(u'hello_bio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=30, null=True, blank=True)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'hello', ['Bio'])


    def backwards(self, orm):
        # Deleting model 'Bio'
        db.delete_table(u'hello_bio')


    models = {
        u'hello.bio': {
            'Meta': {'object_name': 'Bio'},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']