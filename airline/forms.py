from django import forms
from coin.models import Coin
from .models import AirLine,Flight,FlightSchedule,Seat,FlightSeat
from django.forms import ModelForm, DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.admin.widgets import AdminSplitDateTime


class AirLineForm(forms.ModelForm):

    class Meta:
        model = AirLine
        fields = ['name','logo']


class FlightForm(forms.ModelForm):

    class Meta:
        model = Flight
        fields = ['flightNo']


class FlightScheduleForm(forms.ModelForm):
    # departueTime = forms.SplitDateTimeField(widget= AdminSplitDateTime())
    # arrivalTime = forms.SplitDateTimeField()
    class Meta:
        model = FlightSchedule
        fields = [
        # 'origin',
        'departueDate',
        'departueTime',
        # 'destination',
        'arrivalDate',
        'arrivalTime',
        'duration','remarks','status']
        widgets = {
          'departueDate':forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
          'arrivalDate':forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
          'departueTime':forms.TimeInput(attrs={'type': 'time'}),
          'arrivalTime':forms.TimeInput(attrs={'type': 'time'}),
          # 'arrivalTime': AdminSplitDateTime( attrs={'type': 'datetime-local'}),
          # 'arrivalTime': AdminSplitDateTime(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local'}),
            'remarks': forms.TextInput(attrs={'row': '5'}),
        }