from django.urls import path, include
from . import views
from .views import orders_list

app_name = 'orders'
urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('all/', orders_list, name='orders_list'),
]
