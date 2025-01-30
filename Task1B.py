from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
import numpy as np



coordinate = (52.2053, 0.1218)

output = stations_by_distance(build_station_list(), coordinate)



def get_station_names():
        station_names = [station[0].name for station in output]
        return station_names

def get_station_town():
    station_town = [station[0].town for station in output]
    return station_town

final = [(station[0].name, station[0].town, station[1]) for station in output]

print(final[:10])
print(final[-10:])

#print(get_station_town())