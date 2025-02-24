import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
from floodsystem.utils import level_history
from floodsystem.utils import sorted_by_key, current_level


#Typical Range outputs a tuple
'''
station = "Bourton Dickler"
data = run(station)
data_tuples = [line.split() for line in data]
dates = [datetime.strptime(date + " " + time, "%Y-%m-%d %H:%M:%S%z") for date, time, level in data_tuples]
levels = [float(level) for date, time, level in data_tuples]
print(dates)
'''
stations = build_station_list()
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
plot_water_levels(station, dates, levels)
#Station is a  monitoring station object


for s in stations:
    if s.name == station_name:
        station = s
        break

#Find list of 5 stations with highest relative water levels
stations
#Return data for each station over the last 10 days

#Plot the data for each station

