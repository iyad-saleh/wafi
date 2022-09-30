from django import forms
from .models import Account
from django.forms import ModelForm, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['name','account_type' ]

