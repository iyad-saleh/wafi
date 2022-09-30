from django import forms
from .models import Passport
from django.forms import ModelForm, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# 'first_name','last_name','father_name','mother_name','birth_date','birth_place','passport_number','issue_date','issue_end','national_number','photo','nationality','sex','issue_place','author',
class PassportForm(forms.ModelForm):

    class Meta:
        model = Passport
        fields = ['first_name','last_name','father_name','mother_name','birth_date','birth_place','passport_number','issue_date','issue_end','national_number','photo','nationality','sex','issue_place']
        widgets = {
    #         'name': forms.TextInput(attrs={'class': 'form-control'}),
          'birth_date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
          'issue_date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
          'issue_end': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
