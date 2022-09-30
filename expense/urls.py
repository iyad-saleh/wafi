from django.urls import path

from .views import *


urlpatterns = [
    path('', index,name='expense_index'),
    path('expenses/', expense_list, name='expense_list'),
    path('expenses/add', add_expense, name='add_expense'),
    path('expenses/<int:pk>/remove', remove_expense, name='remove_expense'),
    path('expenses/<int:pk>/edit', edit_expense, name='edit_expense'),

]
