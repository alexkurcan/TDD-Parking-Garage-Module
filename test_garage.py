import pytest
from garage import enter_garage

def test_enter_garage_vaild_car_id():
    assert enter_garage(1, 2, 13) == True