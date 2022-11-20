from django.urls import path
from . import views
from .views import contact, shipping_returns

urlpatterns = [
    path('', views.contact, name='contact'),
    path('shipping-returns/', views.shipping_returns, name='shipping-returns'),
]
