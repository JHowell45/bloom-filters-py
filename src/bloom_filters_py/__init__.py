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
    internal_filter: int | None = field(init=False)

    def __post_init__(self):
        self.internal_filter = None

    def add(self, value: Any) -> None:
        pass

    def search(self, value: Any) -> bool:
        pass
