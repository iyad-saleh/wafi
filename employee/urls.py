from django.urls import path

from .views import *


urlpatterns = [
    path('', index,name='employee_index'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/add', add_employee, name='add_employee'),
    path('employees/<int:pk>/remove', remove_employee, name='remove_employee'),
    path('employees/<int:pk>/edit', edit_employee, name='edit_employee'),
    path('empType/', indexType,  name='employeeType'),
    path('empTypes/', employee_Type_list, name='employee_Type_list'),
    path('empType/add', add_employee_Type, name='add_employee_Type'),
    path('empType/<int:pk>/remove', remove_employee_Type, name='remove_employee_Type'),
    path('empType/<int:pk>/edit', edit_employee_Type, name='edit_employee_Type'),
]
