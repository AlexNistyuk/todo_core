import asyncio
import json
import logging

from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError

from infrastructure.config import get_settings
from infrastructure.managers.interfaces import IManager

logger = logging.Logger(__name__)


settings = get_settings()


class KafkaManager(IManager):
    client: AIOKafkaProducer
    url = settings.kafka_url
    topic = settings.kafka_topic

    async def send_message(self, message: dict):
        return await self.client.send(self.topic, json.dumps(message).encode("utf8"))

    @classmethod
    async def connect(cls):
        await asyncio.sleep(10)

        try:
            logger.info("Connect to Kafka")

            cls.client = AIOKafkaProducer(bootstrap_servers=cls.url)
            await cls.client.start()
        except KafkaError as exc:
            logger.error(f"Error while connecting to kafka: {exc}")

    @classmethod
    async def close(cls) -> None:
        await cls.client.stop()

        logger.info("Close kafka connection")
