from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

coordinate = (52.2053, 0.1218)

output = stations_by_distance(build_station_list(), coordinate)

final = [(station[0].name, station[0].town, station[1]) for station in output]

print(final[:10])
print(final[-10:])

#print(get_station_town())