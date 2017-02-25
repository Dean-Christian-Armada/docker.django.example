from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models

from core.model_managers import GetManager

# Create your models here.
class Artist(models.Model):
	name = models.CharField(max_length=255)
	age = models.PositiveSmallIntegerField()
	objects = GetManager()

	# https://docs.djangoproject.com/es/1.9/ref/models/instances/#get-absolute-url
	# Used to pass a location header URL upon post
	def get_absolute_url(self):
		return reverse('artists-detail', kwargs={'artist_id':self.id}) # artist_id came from the URL parameter in the urls.py

	def __unicode__(self):
		return self.name