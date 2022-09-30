from django import forms
from coin.models import Coin
from .models import Ked, Journal
from django.forms import ModelForm



class KedForm(forms.ModelForm):

    class Meta:
        model = Ked
        fields = ['title']




