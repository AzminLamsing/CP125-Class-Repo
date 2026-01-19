def find_bottleneck_index(traceroute):
    largest = 0
    index = 1
    for item in range(1,len(traceroute)):
        x,y = traceroute[item - 1]
        x2,y2 = traceroute[item]
        different = y2 - y
        if different < largest :
            largest = different
            index = item -1
    return index 



# (hop_number, latency_in_ms)
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
