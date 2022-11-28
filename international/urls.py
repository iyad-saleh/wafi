from django.urls import path

from .views import *


urlpatterns = [
    path('', searchAirport,name='searchAirport'),

]
