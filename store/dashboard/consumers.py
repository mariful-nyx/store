import json
from channels.generic.websocket import AsyncWebsocketConsumer

class RealTimeChartConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'dashboard'
        self.room_group_name = f'dashboard_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Close the WebSocket connection
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket and send a response
        data = json.loads(text_data)
        chart_data = {"value": data.get("value")}  # Example data
        
        await self.send(text_data=json.dumps(chart_data))
