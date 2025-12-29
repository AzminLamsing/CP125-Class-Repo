# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    # TODO: Implement this function
    # Return hourly rate based on vehicle and time
    if(vehicle_type == "Electric"):
        vehicles_pay = 2
    elif(vehicle_type == "Hybrid"):
        if(hour_24 >= 22 and hour_24 <= 6):
            vehicles_pay = 2
    else :
        vehicles_pay = 5
    
    return vehicles_pay

display = get_hourly_rate("Electric",2)
display1 = get_hourly_rate("Hybrid",23)
# Test your code here
print("Testing Dynamic Parking Rate...")
print(display)
print(display1)
