from django import forms
from .models import Box
from django.forms import ModelForm


class BoxForm(forms.ModelForm):


    class Meta:
        model = Box
        exclude = ['account', 'author','is_delete','company']
