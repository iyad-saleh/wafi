from django.urls import path

from .views import *


urlpatterns = [
    path('', index,name='account_index'),
    path('accounts/', account_list, name='account_list'),
    # path('accounts/add', add_account, name='add_account'),
    path('accounts/<int:pk>/remove', remove_account, name='remove_account'),
    path('accounts/<int:pk>/edit', edit_account, name='edit_account'),

]
