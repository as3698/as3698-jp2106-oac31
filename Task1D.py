from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

rivers_with_station(build_station_list)

stations_by_river(build_station_list)

x = 'River Aire'
print(stations_by_river(build_station_list, x))
x = 'River Cam'
print(stations_by_river(build_station_list, x))
x = 'River Thames'
print(stations_by_river(build_station_list, x))
