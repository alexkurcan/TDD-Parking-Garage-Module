def enter_garage(garage, car_id, entry_hour):
    if not isinstance(entry_hour, int):
        raise TypeError("entry hour has to be int")

    if car_id in garage["cars"]:
        raise ValueError("that car is already in the garage")

    if len(garage["cars"]) >= garage["capacity"]:
        raise ValueError("garage is full")

    garage["cars"][car_id] = entry_hour

def exit_garage(garage, car_id):
    return "A" not in garage["cars"] == True

def get_available_spots(garage):
    spots = garage["capacity"] - len(garage["cars"])
    return max(0, spots)

def calculate_fee(hours, rate):
    pass