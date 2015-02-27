from django.db import models

# Create your models here.

class AmountUnit (models.Model):
    amount_unit_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.amount_unit_name

class Treatment (models.Model):
    treatment_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.treatment_name

class Feedstock (models.Model):
    feedstock_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.feedstock_name

class Fraction (models.Model):
    fraction_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.fraction_name

class Status (models.Model):
    status_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.status_name

class Location (models.Model):
    building = models.CharField(max_length=128)

    def __unicode__(self):
        return self.building



class Sample (models.Model):
    sample_name = models.CharField(max_length=128)
    comment = models.TextField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    amount_unit = models.ForeignKey(AmountUnit, null=True, blank=True)
    external_id = models.CharField(max_length=128)
    owner_name = models.CharField(max_length=128)
    custodian_name = models.CharField(max_length=128)
    create_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now_add=True)
    treatment = models.ForeignKey(Treatment, null=True, blank=True)
    feedstock = models.ForeignKey(Feedstock, null=True, blank=True)
    fraction = models.ForeignKey(Fraction, null=True, blank=True)
    status = models.ForeignKey(Status, null=True, blank=True)
    location = models.ForeignKey(Location, null=True, blank=True)
    trb_num = models.IntegerField(null=True, blank=True)
    trb_page = models.IntegerField(null=True, blank=True)
    specific_hazard = models.CharField(max_length=128, null=True, blank=True)
    label_description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.sample_name


