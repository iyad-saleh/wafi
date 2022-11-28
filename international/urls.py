from django.urls import path

from .views import (searchAirport,
    AirPortList,CityList, CountryList,
    AirPortCreate,CityCreate,CountryCreate,
    AirPortDeleteView,CityDeleteView,CountryDeleteView
    )


urlpatterns = [
    path('', searchAirport,name='searchAirport'),
    path('CountryList/', CountryList.as_view(),name='CountryList'),
    path('CountryCreate/', CountryCreate.as_view(),name='CountryCreate'),

    path('CityList/', CityList.as_view(),name='CityList'),
    path('CityCreate/', CityCreate.as_view(),name='CityCreate'),

    path('AirPortList/', AirPortList.as_view(),name='AirPortList'),
    path('AirPortCreate/', AirPortCreate.as_view(),name='AirPortCreate'),

]
