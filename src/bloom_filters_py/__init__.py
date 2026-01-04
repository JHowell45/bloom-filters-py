import abc
from hashlib import sha1, sha3_512, sha256
from typing import Any, Callable


class BloomFilterInterface(abc.ABC):
    @abc.abstractmethod
    def add(self, value: Any) -> None: ...

    @abc.abstractmethod
    def search(self, value: Any) -> bool: ...


class BloomFilter(BloomFilterInterface):
    def __init__(self, hash_functions: list[Callable] = []):
        self.hash_functions = (
            hash_functions if hash_functions else [sha1, sha256, sha3_512]
        )
