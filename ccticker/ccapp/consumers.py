# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from django.core.cache import cache


class TickerConsumer(WebsocketConsumer):

    def connect(self):
        cryptocoin = self.scope['url_route']['kwargs']['cryptocoin']
        currency = self.scope['url_route']['kwargs']['currency']
        self.ticker_code = cryptocoin + currency
        async_to_sync(self.channel_layer.group_add)(
            self.ticker_code,
            self.channel_name
        )
        super().connect()
        self.send(text_data=json.dumps({
            'message': f'connected'
        }))
        self.price_update({
            'price': cache.get(self.ticker_code)
        })

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.ticker_code,
            self.channel_name
        )
        super().disconnect(close_code)

    def price_update(self, event):
        price = event['price']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'price': price,
        }))
