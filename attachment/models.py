from django.db import models
from sample.models import Sample
from time import time

# Create your models here.
def get_upload_file_name(instance, filename):
    return "%s_%s" % (str(time()).replace('.', "_"), filename)

class Attachment (models.Model):
    sdms = models.ManyToManyField(Sample,null=True, blank='True')
    path = models.FilePathField(null=True,blank='True')
    filename = models.FileField(upload_to=get_upload_file_name,null=True, blank='True')

    def __unicode__(self):
        return self.filename
