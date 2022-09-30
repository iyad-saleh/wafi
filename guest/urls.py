from django.urls import path
from .views import ( trip,index,
 searchLocation, searchTrip,
    home,flight,sea,visa,hotel,
    document,insurance,about,shipping)

urlpatterns = [
    path('', home, name='home'),
    path('transport/', index, name='transport'),
    path('searchLocation/', searchLocation, name='searchLocation'),
    path('searchTrip/', searchTrip, name='searchTrip'),
    path('trip', trip, name='trip'),
    path('flight/', flight, name='flight'),
    path('sea/', sea, name='sea'),
    path('visa/', visa, name='visa'),
    path('hotel/', hotel, name='hotel'),
    path('insurance/', insurance, name='insurance'),
    path('document/', document, name='document'),
    path('shipping/', shipping, name='shipping'),
    path('about/', about, name='about'),
]
