# payments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('webhook/payments', views.webhook_receiver, name='webhook_receiver'),
    path('payments/<str:payment_id>/events', views.get_payment_events, name='get_payment_events'),
]