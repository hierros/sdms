from django.contrib import admin
from sample.models import Sample, AmountUnit, Treatment, Status, Fraction, Location, Feedstock

# Register your models here.
admin.site.register(Sample)
admin.site.register(AmountUnit)
admin.site.register(Location)
admin.site.register(Treatment)
admin.site.register(Status)
admin.site.register(Fraction)
admin.site.register(Feedstock)