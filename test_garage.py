import pytest
from garage import get_available_spots

def test_get_available_spots_basic():
    garage = {
        "capacity": 10,
        "cars":{}
    }
    assert get_available_spots(garage) == 15