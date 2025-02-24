
from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    output= []
    for station in stations:
        if station.typical_range_consistent() and station.latest_level is not None:
            relative_level = station.relative_water_level()
            if float(relative_level) > float(tol) and relative_level is not None:
                output.append((station.name, relative_level))
                output.sort(key=lambda x: x[1], reverse=True)
    return output

'''
def stations_level_over_threshold(stations, tol):
    output= []
    for station in stations:
        if station.typical_range_consistent() and station.latest_level is not None:
            relative_level = station.relative_water_level()
            if float(relative_level) > float(tol) and relative_level is not None:
                output.append((station.name, relative_level))
                output.sort(key=lambda x: x[1], reverse=True)
    for station in output:
        print(station)
'''

def stations_highest_rel_level(stations, N):
    output= []
    for station in stations:
        if station.typical_range_consistent() and station.latest_level is not None:
            relative_level = station.relative_water_level()
            if relative_level is not None:
                output.append((station.name, relative_level))
                output.sort(key=lambda x: x[1], reverse=True)
        
    return output[:N]
