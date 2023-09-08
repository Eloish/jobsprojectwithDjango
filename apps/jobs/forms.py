from django import forms
from .models import job,application

class Addjobform(forms.ModelForm):
    class Meta:
        model=job
        fields= ['title','description','long_description','company_name','company_address','company_place','company_zipcode','company_country','company_size']

class applicationForm(forms.ModelForm):
    class Meta:
        model=application
        fields=["content","experiences"]
