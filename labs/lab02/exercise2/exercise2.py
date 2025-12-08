# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    tent_need = math.ceil(participants/tent_capacity)
    cost_tent = tent_need * tent_price
    cost_food = participants * meal_price
    total_cost = cost_tent + cost_food

    return total_cost

# Test your code here
print("Testing Camping Logistics...")
