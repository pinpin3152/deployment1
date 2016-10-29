from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.

#https://docs.djangoproject.com/en/1.9/ref/models/fields/#mode-field-types

class EmailManager(models.Manager):
   def addEmail(self, **kwargs):

      if EMAIL_REGEX.match(kwargs['email']):
         results = Email.objects.create(email=kwargs['email'])
         return results

      else:
         return False

   def getAll(self):
      results = Email.objects.all()
      print results
      return results

class Email(models.Model):

   email = models.EmailField()
   created_at = models.DateField(auto_now=True)
   updated_at = models.DateField(auto_now=True)
   objects = EmailManager()
