from typing import Sequence, Any

import pytest

from theperson.person import Person


@pytest.fixture(params=[
    ["apple", "banana", "cherry"],
    [1, 2, 3, 4],
    ["foo", 42, True],
    (10, 20, 30),
    range(3),
])
def sample_iterable(request) -> Sequence[Any]:
    """Fixture for providing various non-empty iterables."""
    return request.param


@pytest.fixture(params=[[], (), ""])
def empty_iterable(request):
    """Fixture for empty iterables."""
    return request.param


def test_choose_set_raises_typeerror():
    with pytest.raises(TypeError):
        Person.choose({1, 2, 3})


def test_choose_dict_raises_keyerror():
    with pytest.raises(KeyError):
        Person.choose({"a": 1})


def test_choose_non_empty(sample_iterable):
    """Test Person.choose on non-empty iterables."""

    result = Person.choose(sample_iterable)
    assert result in sample_iterable


def test_choose_empty_raises_indexerror(empty_iterable):
    """Test Person.choose raises IndexError on empty iterable."""

    with pytest.raises(IndexError):
        Person.choose(empty_iterable)
