
def calculate_base_usage(distance):
    """
    Calculates the base battery usage.
    1.5% battery per 10 meters.
    """
    # TODO: Implement this function
    usage = ((distance/10) * 0.015)
    return usage

def apply_mode_bonus(usage, is_sport_mode):
    """
    Increases battery consumption by 50% if in Sport Mode.
    """
    # TODO: Implement this function
    battery = calculate_base_usage(distance)
    if(is_sport_mode):
        current_battery = battery + (battery * 0.5)
    return current_battery

def has_enough_battery(distance, current_battery, is_sport_mode):
    """
    Calculates if there is enough battery for a round trip (distance * 2).
    """
    # TODO: Implement this function
    total_battery = apply_mode_bonus(usage,is_sport_mode)
    
