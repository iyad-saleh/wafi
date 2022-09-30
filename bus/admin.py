from django.contrib import admin
from .models import Bus#, Driver

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ( 'id',
                'account',
                'company',
                'customer',
                'start_date',
                'busType',
                'busNumber',
                'seats',
                'memo',
                'create_at',
                'author',
                )
    list_filter = (
                'company',
                'customer',
                'busType',
                'seats',
                'update_at',
                'author',
                )

# @admin.register(Driver)
# class DriverAdmin(admin.ModelAdmin):
#     list_display = (
#                 'name',
#                 'status',
#                 'company',
#                 'phoneNumber',
#                 'start_date',
#                 'create_at',
#                 'author',
#                 )
#     list_filter = (
#                 'company',
#                 )
