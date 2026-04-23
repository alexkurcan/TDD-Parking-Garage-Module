def enter_garage(garage, car_id, entry_hour):
    if not isinstance(entry_hour, int):
        raise TypeError("entry hour has to be int")

    if car_id in garage["cars"]:
        raise ValueError("that car is already in the garage")

    if len(garage["cars"]) >= garage["capacity"]:
        raise ValueError("garage is full")

    garage["cars"][car_id] = entry_hour

def exit_garage(garage, car_id):
    if car_id not in garage["cars"]:
        raise KeyError("car could not be found")

def get_available_spots(garage):
    spots = garage["capacity"] - len(garage["cars"])
    return max(0, spots)

def calculate_fee(hours, rate):
    if not isinstance(hours, (int, float)) or not isinstance(rate, (int, float)):
        raise TypeError("hours and rate have to be a number")
    if hours < 0 or rate < 0:
        raise ValueError("hours and rate must be a non-negative number")
    return round(hours * rate, 2)