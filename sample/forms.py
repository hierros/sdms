from django import forms
from sample.models import Sample, Location, AmountUnit, Treatment, Feedstock, Fraction, Status

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['sample_name', 'comment', 'amount', 'amount_unit', 'external_id', 'owner_name', 'custodian_name',
                  'treatment', 'feedstock', 'fraction', 'status', 'trb_num', 'trb_page', 'location',
                  'specific_hazard', 'label_description']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ("Sample",)
        fields = ['building']

class AmountUnitForm(forms.ModelForm):
    class Meta:
        model = AmountUnit
        fields = ['amount_unit_name']

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['treatment_name']

class FeedstockForm(forms.ModelForm):
    class Meta:
        model = Feedstock
        fields = ['feedstock_name']

class FractionForm(forms.ModelForm):
    class Meta:
        model = Fraction
        fields = ['fraction_name']

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields=['status_name']