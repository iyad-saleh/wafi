from django.urls import path

from .views import *


urlpatterns = [
    path('', index,name='passport_index'),
    path('passports/', passport_list, name='passport_list'),
    path('passportList/', PassportList, name='passportList'),
    path('passports/add', add_passport, name='add_passport'),
    path('passports/<int:pk>/remove', remove_passport, name='remove_passport'),
    path('passports/<int:pk>/edit', edit_passport, name='edit_passport'),
    path('passports/<int:id>/photo/<int:pk>/remove', remove_photo, name='remove_photo'),
    path('passports/searchPassport/', searchPassport, name='searchPassport'),
]
