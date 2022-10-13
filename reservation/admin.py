from django.contrib import admin
from .models import  Reservation_airline,Reservation

# @admin.register(Reservation)
# class ReservationAdmin(admin.ModelAdmin):
#     list_display = (
#                 'title',
#                 'reservation_type',
#                 'Date',
#                 'PNR',
#                 'trip',
#                 'vendor',
#                 'customer',
#                 'pay_price',
#                 'pay_coin',
#                 'sell_price',
#                 'sell_coin',
#                 'status',
#                 'company',
#                 'create_at',
#                 'author',

#                 )
#     list_filter = (
#          'reservation_type',
#                 'company',
#                 'author',
#                 )

@admin.register(Reservation_airline)
class Reservation_airlineAdmin(admin.ModelAdmin):
    list_display = (

              'passenger_num',
                'title','Date','supplier',
                'customer','pay_price',
                'pay_coin','sell_price',
                'sell_coin','status',
                'PNR','departure_date',
                'airline_company','flight_no',
                'departure','arrival','roundtrip',
                'get_passport','flight_type','return_date',

                'company',
                'created_at',
                'author',)
    list_filter=('company','author',
        )
    def get_passport(self, obj):
        return "\n".join([p.passport_number for p in obj.passport.all()])