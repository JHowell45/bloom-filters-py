from hashlib import sha1, sha256, sha512
from typing import Any

import pytest

from bloom_filters_py import BloomFilter


def test_add():
    size: int = 5
    filter = BloomFilter([sha1], size)
    assert filter.internal_filter == 1 << size
    v = "Hello, World!"
    filter.add(v)
    expected = 1 << 5
    expected |= 1 << int(sha1(v.encode("utf-8")).hexdigest(), 16) % filter.size
    print(bin(expected))
    assert filter.internal_filter == expected


@pytest.mark.parametrize("test_value", ["a", "Hello, World!"])
def test_search_exists(test_value: Any):
    filter = BloomFilter([sha1, sha256, sha512], 10)
    filter.add(test_value)
    assert filter.search(test_value)


testdata = [
    [["on", "a", "long"], "Hello"],
    [["on", "a", "long"], "list"],
    [["on", "a", "long"], "b"],
    [["on", "a", "long"], "off"],
]


@pytest.mark.parametrize("data,not_exist", testdata)
def test_search_does_not_exist(data: list, not_exist: Any):
    filter = BloomFilter([sha1, sha256, sha512], 40)
    for v in data:
        filter.add(v)
    assert not filter.search(not_exist)
