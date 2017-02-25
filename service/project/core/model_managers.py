from __future__ import unicode_literals

from django.db import models

# Create your models here.

# http://stackoverflow.com/questions/1512059/django-get-an-object-form-the-db-or-none-if-nothing-matches 
class GetManager(models.Manager):
    #Adds get_or_none method to objects with more flexibility than get_object_or_404
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None