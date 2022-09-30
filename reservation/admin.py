from django.contrib import admin
from .models import Reservation, SubReservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
                'title',
                'reservation_type',
                'Date',
                'PNR',
                'trip',
                'vendor',
                'customer',
                'pay_price',
                'pay_coin',
                'sell_price',
                'sell_coin',
                'status',
                'company',
                'create_at',
                'author',

                )
    list_filter = (
         'reservation_type',
                'company',
                'author',
                )

@admin.register(SubReservation)
class SubReservationAdmin(admin.ModelAdmin):
    list_display = (

                'passport',
                'reservation',
                'priveat_no1',
                'priveat_no2',
                'pay_price',
                'pay_coin',
                'sell_price',
                'sell_coin',
                'company',
                'create_at',
                'author',)
    list_filter=('company','author',
        )