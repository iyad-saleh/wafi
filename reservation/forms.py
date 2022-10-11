from django import forms
from .models import Reservation, Reservation_airline
from django.forms import ModelForm


# 'title','Date','supplier','customer','pay_price','pay_coin','sell_price','sell_coin','status'
class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = [
                'title','Date','supplier',
                'customer','pay_price',
                'pay_coin','sell_price',
                'sell_coin','status']
        widgets = {
            'Date': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local'}),
        }

# 'PNR','departure_date','airline_company','flight_no','departure','arrival','roundtrip','passport','flight_type','return_date'


class AirlineReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation_airline
        fields = ['passenger_num',
                'title','Date','supplier',
                'customer','pay_price',
                'pay_coin','sell_price',
                'sell_coin','status',
                'PNR','departure_date',
                'airline_company','flight_no',
                'departure','arrival','roundtrip',
                'passport','flight_type','return_date'
                ]
        widgets = {
            'Date': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local'}),
            'return_date': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local'}),
            'departure_date': forms.DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local'}),
        }



# class SubReservationForm(forms.ModelForm):

#     class Meta:
#         model = SubReservation
#         fields = ['passport','priveat_no1','priveat_no2','pay_price','pay_coin','sell_price','sell_coin',]
