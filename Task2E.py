import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from floodsystem.utils import level_history
from floodsystem.utils import sorted_by_key, current_level
from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation



#Typical Range outputs a tuple
'''
station = "Bourton Dickler"
data = run(station)
data_tuples = [line.split() for line in data]
dates = [datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M:%S%z") for date, time, level in data_tuples]
levels = [float(level) for date, time, level in data_tuples]
print(dates)
'''

'''
data = level_history(station)
dates = data[0]
levels = data[1]
station_name = "Bourton Dickler"
station = None

#def highest_level(stations):



for s in stations:
    if s.name == station_name:
        station = s
        break
'''

#Station is a  monitoring station object
number = 5
days = 10
n = 0
stations = build_station_list()
update_water_levels(stations)
#Find list of 5 stations with highest relative water levels
danger_stations = stations_highest_rel_level(stations, number)
station_names = [station[0] for station in danger_stations]
station_levels = [station[1] for station in danger_stations]
station = None
#Return data for each station over the last 10 days
for object in station_names:
    for s in stations:
        if s.name == station_names[n]:
            station = s
            break
    n += 1
   
    dates, levels = level_history(station.name, days)
    plot_water_levels(station, dates, levels)
    
#Plot the data for each station

