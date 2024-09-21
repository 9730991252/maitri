from django.urls import path
from . import views
urlpatterns = [
    path('bill_award', views.bill_award, name='bill_award'),
    path('item_list', views.item_list, name='item_list'),
    path('size_edit', views.size_edit, name='size_edit'),
]