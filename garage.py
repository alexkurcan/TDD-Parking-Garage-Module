def enter_garage(garage, car_id, entry_hour):
    pass

def exit_garage(garage, car_id):
    pass

def get_available_spots(garage):
    spots = garage["capacity"] - len(garage["cars"])
    return max(0, spots)

def calculate_fee(hours, rate):
    pass