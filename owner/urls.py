from django.urls import path
from . import views
urlpatterns = [
    path('owner_login/', views.owner_login, name='owner_login'),
    path('owner_home/', views.owner_home, name='owner_home'),
    path('add_item/', views.add_item, name='add_item'),
    path('add_bill/', views.add_bill, name='add_bill'),
]