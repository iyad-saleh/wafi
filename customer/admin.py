from django.contrib import admin

from .models import Customer

# admin.site.register(Company)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ( 'id',
                'account',
                'logo',
                'get_address',
                'phoneNumber1',
                'phoneNumber2',
                'get_tradeRecord',
                'email',

                'webSite',
                'client',
                'aircompany',
                'transportcompany',
                'seacompany',
                'visacompany',
                'backagecompany',
                'hotelcompany',
                'insurancecompany',
                'documentcompany',
                'shippingcompany',
                'author',
                )
    list_filter = (


                'author',
                )

    def get_tradeRecord(self, obj):
        if obj.tradeRecord:
            return obj.tradeRecord[:10]+'...'
    def get_address(self, obj):
        if obj.address:
            return obj.address[:10]+'...'











