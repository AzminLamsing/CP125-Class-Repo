def find_station(stations, name):
    for item in range (len(stations)):
        if stations[item] == name :
            return name 
    return -1

                    
def count_stops(stations, start, stop):
    start_index = find_station(stations,start)
    stop_index = find_station(stations,stop)
     
    if start_index == -1 or stop_index == -1:
        return -1
    else :
        count = start_index - stop_index
        return count
