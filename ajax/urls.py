from django.urls import path
from . import views
urlpatterns = [
    path('bill_award', views.bill_award, name='bill_award'),
]