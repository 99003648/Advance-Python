import pytest
from Problem import Temperature


@pytest.fixture
def get_t1():
    return Temperature(35)


@pytest.fixture
def get_t2():
    return Temperature(22)


def test_equal(get_t1, get_t2):
    assert (get_t1 == get_t2) == False


def test_lesser(get_t1, get_t2):
    assert (get_t1 < get_t2) == False
