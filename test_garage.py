import pytest
from garage import get_available_spots

def test_get_available_spots_empty():
    garage = {
        "capacity": 10,
        "cars":{}
    }
    assert get_available_spots(garage) == 10

def test_get_available_spots_partial():
    garage = {
        "capacity": 10,
        "cars":{"A": 1}
    }
    assert get_available_spots(garage) == 9

def test_get_available_spots_full():
    garage = {
        "capacity": 10,
        "cars": {"A": 1}
    }
    assert get_available_spots(garage) == 0