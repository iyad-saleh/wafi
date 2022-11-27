from django.urls import path

from .views import *


urlpatterns = [
    # path('reservation/', reservation_index,name='reservation_index'),
    # path('reservation_list/', reservation_list, name='reservation_list'),
    # path('reservation/add', add_reservation, name='add_reservation'),
    # path('reservation/<int:pk>/remove', remove_reservation, name='remove_reservation'),
    # path('reservation/<int:pk>/edit', edit_reservation, name='edit_reservation'),



    path('airline/', airline_index,name='airline_index'),
    # path('airline_list/', airline_list, name='airline_list'),
    # path('airline/add', add_airline, name='add_airline'),
    # path('airline/<int:pk>/remove', remove_airline, name='remove_airline'),
    # path('airline/<int:pk>/edit', edit_airline, name='edit_airline'),
]
