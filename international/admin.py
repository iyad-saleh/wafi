from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from  .models import Country,  AirPort,City

class Country_Admin(ImportExportModelAdmin):
    list_display = ('id','name_ar','name_en','Alpha_2','Alpha_3','currency_alphabetic','currency_name','Arabic_Formal')
    search_fields =('name_en','name_ar')
    class Meta:
        model = Country
admin.site.register(Country,Country_Admin)


# class Currency_Admin(ImportExportModelAdmin):
#     list_display = ('id','short_title','long_title')

#     class Meta:
#         model = Currency
# admin.site.register(Currency,Currency_Admin)


class AirPort_Admin(ImportExportModelAdmin):
    list_display = ('ident','airport_type','name','iso_country','iso_region','municipality','iata_code')
    search_fields =('iso_country__name_en','iata_code','municipality__city_ascii')#'elevation_ft','continent','gps_code',,'local_code','coordinates'
    list_filter = ('airport_type', 'iso_country__name_en')
    list_per_page = 100
    class Meta:
        model = AirPort
admin.site.register(AirPort,AirPort_Admin)


class City_Admin(ImportExportModelAdmin):
    list_display = ('city','city_ascii','country','iso2','iso3')
    search_fields =('country__name_en','city')
    list_filter = ('country__name_en',)
    list_per_page = 20
    class Meta:
        model = City
admin.site.register(City,City_Admin)


