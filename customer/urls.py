from django.urls import path

from .views import *


urlpatterns = [
    path('', index,name='customer_index'),
    path('customers/', customer_list, name='customer_list'),
    path('customers/add', add_customer, name='add_customer'),
    path('customers/<int:pk>/remove', remove_customer, name='remove_customer'),
    path('customers/<int:pk>/edit', edit_customer, name='edit_customer'),

]
