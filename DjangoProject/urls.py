from django.contrib import admin
from django.urls import path, include

import cart.views
from accounts import views
from accounts.views import SignUp

urlpatterns = [
    path('admin/', admin.site.urls),

    path('orders/', include('orders.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', SignUp.as_view(), name='register'),
    path('home', views.home, name='home'),
    path('cart/', include('cart.urls', namespace='cart')),

    path('products', cart.views.product_list, name='product_list'),

]
