from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='airline'),
    path('airline/', airline_list, name='airline_list'),
    path('airline/add', add_airline, name='add_airline'),
    path('airline/<int:pk>/remove', remove_airline, name='remove_airline'),
    path('airline/<int:pk>/edit', edit_airline, name='edit_airline'),

    path('<int:airline_pk>/', flight_index, name='flight_index'),
    path('<int:airline_pk>/flight', flight_list, name='flight_list'),
    path('<int:airline_pk>/flight/add', add_flight, name='add_flight'),
    path('<int:airline_pk>/flight/<int:pk>/remove', remove_flight, name='remove_flight'),
    path('<int:airline_pk>/flight/<int:pk>/edit', edit_flight, name='edit_flight'),


    path('schedule/',schedule,name='schedule'),
    path('<int:airline_pk>/<int:flight_pk>', schedule_index, name='schedule_index'),
    path('<int:airline_pk>/<int:flight_pk>/schedule', schedule_list, name='schedule_list'),
    path('<int:airline_pk>/<int:flight_pk>/schedule/add', add_schedule, name='add_schedule'),
    path('<int:airline_pk>/<int:flight_pk>/schedule/<int:pk>/remove', remove_schedule, name='remove_schedule'),
    path('<int:airline_pk>/<int:flight_pk>/schedule/<int:pk>/edit', edit_schedule, name='edit_schedule'),
]
