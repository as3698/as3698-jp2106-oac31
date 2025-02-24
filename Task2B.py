from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold 
from floodsystem.stationdata import update_water_levels
  
tol = 0.8
stations = build_station_list()
update_water_levels(stations)
print(stations_level_over_threshold(stations, tol))