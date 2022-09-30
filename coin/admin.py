from django.contrib import admin
from .models import Coin
from import_export.admin import ImportExportModelAdmin



@admin.register(Coin)
class CoinAdmin(ImportExportModelAdmin):

    list_display = ( 'id',
                'short_title',
                'long_title',
                'active',
                )
