import pytest
from garage import get_available_spots, enter_garage, exit_garage

# --------- For enter_garage func ---------
def test_enter_garage_sucess():
    garage = {
        "capacity": 2,
        "cars":{"A": 1}
    }
    assert "A" in garage["cars"]

def test_enter_garage_duplicate():
    garage = {
        "capacity": 2,
        "cars":{"A":1}
    }
    with pytest.raises(ValueError):
        enter_garage(garage, "A", 2)

def test_enter_garage_invaild_time():
    garage = {
        "capacity": 2,
        "cars":{}
    }
    with pytest.raises(TypeError):
        enter_garage(garage, "A", "2")

# --------- For exit_garage func ---------
def test_exit_garage_success():
    garage = {
        "capacity": 2,
        "cars":{"A": 1}
    }
    exit_garage(garage, "A")
    assert "A" not in garage["cars"]

def test_exit_garage_not_found():
    garage = {
        "capacity": 2,
        "cars":{}
    }
    with pytest.raises(KeyError):
        exit_garage(garage, "A")

# --------- For get_avaiable_spots func ---------
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
        "capacity": 0,
        "cars": {"A": 1}
    }
    assert get_available_spots(garage) == 0

def test_enter_garage_full():
    garage = {
        "capacity":1,
        "cars":{"A":1}
    }
    with pytest.raises(ValueError):
        enter_garage(garage, "B", 2)