from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name','logo','address','phoneNumber1','phoneNumber2','phoneNumber3','phoneNumber4','tradeRecord','email','webSite',]
