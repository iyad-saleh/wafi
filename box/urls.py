from django.urls import path

from .views import *


urlpatterns = [
    path('', index,name='box_index'),
    path('boxs/', box_list, name='box_list'),
    path('boxs/add', add_box, name='add_box'),
    path('boxs/<int:pk>/remove', remove_box, name='remove_box'),
    path('boxs/<int:pk>/edit', edit_box, name='edit_box'),

]
