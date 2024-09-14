from django.urls import path
from . import views
urlpatterns = [
    path('customer_home/', views.customer_home, name='customer_home'),
    path('lucky_draw/<int:bill_id>', views.lucky_draw, name='lucky_draw'),
]