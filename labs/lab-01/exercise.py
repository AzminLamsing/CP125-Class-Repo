print("Hello everyone, Lab 01")



# Customer 1 - Nasi Lemak
price1 = 8.50
tax1 = price1 * 0.06  # 6% SST tax
service1 = 2.00
total1 = price1 + tax1 + service1
print(f"Customer 1 total: RM{total1:.2f}")

# Customer 2 - Roti Canai
price2 = 3.50
tax2 = price2 * 0.06  # 6% SST tax
service2 = 2.00
total2 = price2 + tax2 + service2
print(f"Customer 2 total: RM{total2:.2f}")

# Customer 3 - Mee Goreng
price3 = 7.00
tax3 = price3 * 0.06  # 6% SST tax
service3 = 2.00
total3 = price3 + tax3 + service3
print(f"Customer 3 total: RM{total3:.2f}")

# Define the function once
def calculate_bill(meal_price):
    tax = meal_price * 0.08  # 8% SST tax
    service_charge = 2.00
    total = meal_price + tax + service_charge
    return total

# Now reuse it for each customer
total1 = calculate_bill(8.50)  # Nasi Lemak
print(f"Customer 1 total: RM{total1:.2f}")

total2 = calculate_bill(3.50)  # Roti Canai
print(f"Customer 2 total: RM{total2:.2f}")

total3 = calculate_bill(7.00)  # Mee Goreng
print(f"Customer 3 total: RM{total3:.2f}")

def add_with_print(a, b):
    result = a + b
    print(result)  # Displays the number on screen

def add_with_return(a, b):
    result = a + b
    return result  # Gives back the number

# Test 1: Using print
x = add_with_print(5, 3)
print(f"x contains: {x}")

# Test 2: Using return
y = add_with_return(5, 3)
print(f"y contains: {y}")

# Calculating areas without factorization
pi = 3.14159

# Circle 1
radius1 = 5
area1 = pi * radius1 * radius1
print(f"Circle 1 (radius {radius1}): Area = {area1:.2f}")

# Circle 2
radius2 = 10
area2 = pi * radius2 * radius2
print(f"Circle 2 (radius {radius2}): Area = {area2:.2f}")

# Circle 3
radius3 = 7
area3 = pi * radius3 * radius3
print(f"Circle 3 (radius {radius3}): Area = {area3:.2f}")


def get_student_data():
    name = input("Enter student name: ")
    score = int(input("Enter score: "))
    return name, score

def determine_status(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"

def display_results(name, score, status):
    print(f"Student: {name}")
    print(f"Score: {score}")
    print(f"Status: {status}")

# Use them together
student_name, student_score = get_student_data()
student_status = determine_status(student_score)
display_results(student_name, student_score, student_status)

