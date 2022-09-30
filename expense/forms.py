from django import forms
from .models import Expense
from django.forms import ModelForm, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class ExpenseForm(forms.ModelForm):


    class Meta:
        model = Expense
        exclude = ['account', 'author','is_delete','company']
