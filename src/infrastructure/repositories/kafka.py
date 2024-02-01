import json

from infrastructure.config import get_settings
from infrastructure.managers.kafka import KafkaManager


class KafkaRepository(KafkaManager):
    topic = get_settings().kafka_topic

    async def send_message(self, message: dict):
        return await self.client.send(self.topic, json.dumps(message).encode("utf8"))
