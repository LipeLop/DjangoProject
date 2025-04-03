from django.contrib import admin

from django.contrib import admin
from MySqlDjango.models import Customer, Order
admin.site.register(Customer)
admin.site.register(Order)