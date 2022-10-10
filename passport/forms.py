from django import forms
from .models import Passport, Passenger, Photo
from django.forms import ModelForm, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.forms.models import inlineformset_factory



# 'first_name','last_name','father_name','mother_name','birth_date','birth_place','national_number','nationality','img','gender','phone','mobile','email',
# 'passport_number','issue_date','issue_end','photo','issue_place',

class  PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name','last_name','father_name',
                   'mother_name','birth_date','birth_place',
                   'national_number','nationality',
                    'gender','phone','mobile','email','avatar']
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
                    'issue_end', 'issue_place','avatar']
        widgets = {
    #         'name': forms.TextInput(attrs={'class': 'form-control'}),
          'birth_date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
          'issue_date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
          'issue_end': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

PhotoFormSet= inlineformset_factory(Passport,  # parent form
                                      Photo,  # inline-form
                                      fields=['image',], # inline-form fields
                                      # set to false because cant' delete an non-exsitant instance
                                      can_delete=False,
                                      # how many inline-forms are sent to the template by default
                                       extra=4)

class PhotoForm(forms.ModelForm):


    class Meta:
        model = Photo
        fields=['image',]