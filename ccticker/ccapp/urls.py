from django.urls import path

from .consumers import TickerConsumer
from .views import TickerView

urlpatterns = [
    path('', TickerView.as_view()),
]

websocket_urlpatterns = [
    path('ws/<str:cryptocoin>/<str:currency>', TickerConsumer),
]
