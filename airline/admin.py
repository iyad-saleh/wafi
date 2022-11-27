from django.contrib import admin

from .models import AirLine

# admin.site.register(Company)
@admin.register(AirLine)
class AirLineAdmin(admin.ModelAdmin):

    list_display = ( 'id',
                'name',
                'logo',)