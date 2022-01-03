from django.urls import path
from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/bill-room/', WSConsumer.as_asgi())
]