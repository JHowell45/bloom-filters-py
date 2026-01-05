import abc
from dataclasses import dataclass, field
from hashlib import sha1, sha3_512, sha256
from typing import Any, Callable


class BloomFilterInterface(abc.ABC):
    @abc.abstractmethod
    def add(self, value: Any) -> None: ...

    @abc.abstractmethod
    def search(self, value: Any) -> bool: ...


@dataclass
class BloomFilter(BloomFilterInterface):
    hash_functions: list[Callable] = field(
        default_factory=lambda: [sha1, sha256, sha3_512]
    )
    size: int = field(default=100)
    internal_filter: int = field(init=False)

    def __post_init__(self):
        self.internal_filter = 1 << self.size

    def add(self, value: Any) -> None:
        for hash_f in self.hash_functions:
            idx: int = self.__hash_index(hash_f, value)
            self.internal_filter |= 1 << idx

    def search(self, value: Any) -> bool:
        for hash_f in self.hash_functions:
            idx: int = self.__hash_index(hash_f, value)
            search_bit = self.internal_filter & (1 << idx)
            if search_bit >> idx == 0:
                return False
        return True

    def __hash_index(self, hash: Callable, value: Any) -> int:
        if type(value) is str:
            value = value.encode("utf-8")
        return int(hash(value).hexdigest(), 16) % self.size
