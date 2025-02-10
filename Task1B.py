#This code is used to find the closest stations to a given point
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

coordinate = (52.2053, 0.1218)

stations = build_station_list()


def closest_stations(stations, coordinate):
    output = stations_by_distance(stations, coordinate)

    final = [(station[0].name, station[0].town, round(station[1], 2)) for station in output]

    return final


x = closest_stations(stations, coordinate)
print(x[:10])
print(x[-10:])

