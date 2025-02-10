from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

coordinate = (52.2053, 0.1218)




def closest_stations(coordinate):
    output = stations_by_distance(build_station_list(), coordinate)

    final = [(station[0].name, station[0].town, round(station[1], 2)) for station in output]

    return final


x = closest_stations(coordinate)
print(x[:10])
print(x[-10:])