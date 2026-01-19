def find_largest_drop(readings):
    largest_drop = 0
    for item in range(len(readings)-1):
        if readings[item] > readings[item + 1]:
            drop = abs(readings[item] - readings[item + 1])
            if drop > largest_drop :
                largest_drop = drop 
    return largest_drop      

# Test
temps = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5
