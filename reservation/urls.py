from django.urls import path

from .views import *


urlpatterns = [
    path('', index,name='reservation_index'),
    path('reservations/', reservation_list, name='reservation_list'),
    path('reservations/add', add_reservation, name='add_reservation'),
    path('reservations/<int:pk>/remove', remove_reservation, name='remove_reservation'),
    path('reservations/<int:pk>/edit', edit_reservation, name='edit_reservation'),
]
