from django.urls import path

from .views import *


urlpatterns = [
    path('', index,name='passport_index'),
    path('passports/', passport_list, name='passport_list'),
    path('passports/add', add_passport, name='add_passport'),
    path('passports/<int:pk>/remove', remove_passport, name='remove_passport'),
    path('passports/<int:pk>/edit', edit_passport, name='edit_passport'),

]
