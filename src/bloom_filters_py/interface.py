import abc
from typing import Any



class BloomFilterInterface(abc.ABC):
    @abc.abstractmethod
    def add(self, value: Any) -> None: ...

    @abc.abstractmethod
    def search(self, value: Any) -> bool: ...
