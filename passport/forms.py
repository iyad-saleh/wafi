from django import forms
from .models import Passport, Passenger, Photo
from django.forms import ModelForm, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



# 'first_name','last_name','father_name','mother_name','birth_date','birth_place','national_number','nationality','img','gender','phone','mobile','email',
# 'passport_number','issue_date','issue_end','photo','issue_place',

class  PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name','last_name','father_name',
                   'mother_name','birth_date','birth_place',
                   'national_number','nationality',
                    'gender','phone','mobile','email',]
        widgets = {
    #         'name': forms.TextInput(attrs={'class': 'form-control'}),
          'birth_date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }


class PassportForm(forms.ModelForm):


    class Meta:
        model = Passport
        fields = ['first_name','last_name','father_name',
                   'mother_name','birth_date','birth_place',
                   'national_number','nationality',
                    'gender','phone','mobile','email',
                    'passport_number','issue_date',
                    'issue_end', 'issue_place']
        widgets = {
    #         'name': forms.TextInput(attrs={'class': 'form-control'}),
          'birth_date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
          'issue_date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
          'issue_end': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }


class PhotoForm(forms.ModelForm):


    class Meta:
        model = Photo
        fields=['image',]