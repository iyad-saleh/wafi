from django import forms
from coin.models import Coin
from .models import Customer
from django.forms import ModelForm, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['logo','address','phoneNumber1','phoneNumber2','tradeRecord','email','client','aircompany','transportcompany','seacompany','visacompany','backagecompany','aircompany','hotelcompany','insurancecompany','documentcompany','shippingcompany','webSite']




