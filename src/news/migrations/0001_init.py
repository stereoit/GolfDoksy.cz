# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'News'
        db.create_table('news_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('text_html', self.gf('django.db.models.fields.TextField')(null=True)),
            ('published', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('published_by', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('news', ['News'])


    def backwards(self, orm):
        
        # Deleting model 'News'
        db.delete_table('news_news')


    models = {
        'news.news': {
            'Meta': {'object_name': 'News'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'published_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_html': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['news']
