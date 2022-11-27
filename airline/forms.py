from django import forms
from coin.models import Coin
from .models import AirLine,Flight,FlightSchedule,Seat,FlightSeat
from django.forms import ModelForm, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



class AirLineForm(forms.ModelForm):

    class Meta:
        model = AirLine
        fields = ['name','logo']


class FlightForm(forms.ModelForm):

    class Meta:
        model = Flight
        fields = ['flightNo']


class FlightScheduleForm(forms.ModelForm):

    class Meta:
        model = FlightSchedule
        fields = ['origin','destination','departueTime','arrivalTime','duration','remarks','status']
        widgets = {
          'departueTime':forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local'}),
          'arrivalTime': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local'}),
            'remarks': forms.TextInput(attrs={'row': '5'}),
        }