import pytest

from bloom_filters_py import BloomFilter


def test_add():
    filter = BloomFilter()
    assert filter.internal_filter is None
