from django import forms
from .models import Reservation, SubReservation
from django.forms import ModelForm

# 'title','reservation_type','Date','PNR','trip','vendor','customer','pay_price','pay_coin','sell_price','sell_coin','status',

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['title','reservation_type','Date','PNR','trip','vendor','customer','pay_price','pay_coin','sell_price','sell_coin','status',]
        widgets = {
            'Date': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local'}),
        }

class SubReservationForm(forms.ModelForm):

    class Meta:
        model = SubReservation
        fields = ['passport','priveat_no1','priveat_no2','pay_price','pay_coin','sell_price','sell_coin',]
