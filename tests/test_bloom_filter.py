from hashlib import sha1

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
