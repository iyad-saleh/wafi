from django.urls import path

from .views import *


urlpatterns = [
    path('', index,name='ked_index'),
    path('keds/', ked_list, name='ked_list'),
    path('keds/add', add_ked, name='add_ked'),
    path('keds/<int:pk>/remove', remove_ked, name='remove_ked'),
    path('keds/<int:pk>/edit', edit_ked, name='edit_ked'),
    path('journal', journal_index,name='journal_index'),
    path('journals/', journal_list, name='journal_list'),
    # path('journals/add', add_journal, name='add_journal'),
    # path('journals/<int:pk>/remove', remove_journal, name='remove_journal'),
    # path('journals/<int:pk>/edit', edit_journal, name='edit_journal'),
]
