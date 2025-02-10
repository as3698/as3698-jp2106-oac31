# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

import numpy as np
from floodsystem.utils import sorted_by_key
from haversine import haversine
from floodsystem.stationdata import build_station_list
from List_of_stations import List_of_stations

#Task D
def rivers_with_station(stations):
    from floodsystem.stationdata import build_station_list
    
    stations_d = set()
    for station in stations:
        if station.river:
            stations_d.add(station.river)
    return(stations_d)

    
    

def stations_by_river(stations):
    stations_ra = {}
    for station in stations:
        if station.river:
            if station.river in stations_ra:
                cur_lst = stations_ra[station.river]
                cur_lst.append(station.name)
                stations_ra.update({station.river: cur_lst})
            else:
                stations_ra.update({station.river: [station.name]})
    
    return(stations_ra)


def rivers_by_station_number(stations, N):
    rivers_station_count = {}
    for station in stations:
        if station.river:
            rivers_station_count[station.river] = rivers_station_count.get(station.river, 0) + 1
    river_list = list(rivers_station_count.items())
    river_list.sort(key=lambda x: x[1], reverse=True)
    return((river_list)[:N])
    
#This is used for 1B to find the stations by distance from a given point
def stations_by_distance(stations, p):
    #radius = 6378
    #This function is supposed to calculate the distance between two points
    distances = []
    
    for station in stations:
        lat_1 = p[0]
        lon_1 = p[1]
        lat_2 = station.coord[0]
        lon_2 = station.coord[1]
        #distance = 2 * radius * np.arcsin(np.sqrt(np.sin((lat_2 - lat_1) / 2)**2 + np.cos(lat_1) * np.cos(lat_2) * np.sin((lon_2 - lon_1) / 2)**2))
        distance = haversine((lat_1, lon_1), (lat_2, lon_2))
        distances.append((station, float(distance)))
    sorted_data = sorted_by_key(distances, 1)
    
    return sorted_data

#This is used for 1C to find the stations within a certain radius of a given point
def stations_within_radius(stations, centre, r):
    within = []
    #radius = 6378
    for station in stations:
        lat_1 = (centre[0])
        lon_1 = (centre[1])
        lat_2 = (station.coord[0])
        lon_2 = (station.coord[1])
        distance_c = haversine((lat_1, lon_1), (lat_2, lon_2))
        #distance_c = 2 * radius * np.arcsin(np.sqrt(np.sin((lat_2 - lat_1) / 2)**2 + np.cos(lat_1) * np.cos(lat_2) * np.sin((lon_2 - lon_1) / 2)**2))
        if distance_c <= r:
            within.append((station, float(distance_c)))
    return within
    



   
    




    # python3 -m floodsystem.geo