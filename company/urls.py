from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='company'),
    path('companys/', company_list, name='company_list'),
    path('companys/add', add_company, name='add_company'),
    path('companys/<int:pk>/remove', remove_company, name='remove_company'),
    path('companys/<int:pk>/edit', edit_company, name='edit_company'),
    path('', index, name='company_index'),
    path('users/', user_list, name='user_list'),
    path('users/add', add_user, name='add_user'),
    path('users/<int:pk>/remove', remove_user, name='remove_user'),
    path('users/<int:pk>/edit', edit_user, name='edit_user'),
]
