from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold 
from floodsystem.stationdata import update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np

'''
The program works by finding the stations with higher relative water-level, relative to the typical range
Based on how high above the typical range this value is, the stations are grouped into low, medium,
and high/severe categories. The data from the past 24 hours is then checked for the high/severe categories,
to see if the water level is currently increasing or decreasing, by carrying out a linear correlation
check.
'''
tol = 0.8
low_stations = []
moderate_stations = []
high_stations = []
high_severe_stations = []
severe_stations = []
stations = build_station_list()
update_water_levels(stations)
things = stations_level_over_threshold(stations, tol)
all_stations = []
#The following part splits the stations into categories, depending on how high the relative level is.
for station_name, relative_level in things:
    if 0.8 < relative_level <= 1.0:
        low_stations.append(station_name)
    if 1.0 < relative_level <= 1.3:
        moderate_stations.append(station_name)
    if relative_level > 1.3:
        high_severe_stations.append(station_name)

# this obtains a list of the station data for the stations in the high/severe category
for station in stations:
    if station.name in high_severe_stations:
        all_stations.append(station)

#this checks the extent of positive correlation over the past 24 hours
for station in all_stations:
    dt = 1
    dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
    x = np.arange(len(levels))
    y = np.array(levels)
    if len(x) != 0:
        corel = np.corrcoef(x, y)
        if corel[0,1] < 0.5:
            high_stations.append(station.name)
        else:
            severe_stations.append(station.name)
    #ensures that if there is no past history data, then the station is put in the severe category, to be safe
    else:
        severe_stations.append(station.name)


low_towns = []
moderate_towns = []
high_towns = []
severe_towns = []

#This finds the town from the station data
for station in stations:
    if station.name in low_stations and station.town not in low_towns and station.town != None:
        low_towns.append(station.town)
    if station.name in moderate_stations and station.town not in moderate_towns and station.town != None:
        moderate_towns.append(station.town)
    if station.name in high_stations and station.town not in high_towns and station.town != None:
        high_towns.append(station.town)
    if station.name in severe_stations and station.town not in severe_towns and station.town != None:
        severe_towns.append(station.town)

print('Low risk towns: ' + str(low_towns))
print('Moderate risk towns: ' + str(moderate_towns))
print('High risk towns: ' + str(high_towns))
print('Severe risk towns: ' + str(severe_towns))