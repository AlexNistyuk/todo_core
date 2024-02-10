from abc import ABC, abstractmethod


class IRepository(ABC):
    """Abstract repository"""

    @abstractmethod
    async def insert(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_by_id(self, *args, **kwargs):
        raise NotImplementedError
