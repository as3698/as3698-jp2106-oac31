# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

import numpy as np
from .utils import sorted_by_key
from haversine import haversine

def rivers_with_station(stations):
    from floodsystem.stationdata import build_station_list
    stations = build_station_list()
    stations_d = set()
    for station in stations:
        if station.river:
            stations_d.add(station.river)
    print("Number of rivers with at least one monitoring station:", len(stations_d))
    print(sorted(stations_d)[:10])

def stations_by_river(stations):
    from floodsystem.stationdata import build_station_list
    stations = build_station_list()
    stations_ra = set()
    stations_rc = set()
    stations_rt = set()
    for station in stations:
        if station.river == 'River Aire':
            stations_ra.add(station.name)
    print("Stations by River Aire:",sorted(stations_ra))
    for station in stations:
        if station.river == 'River Cam':
            stations_rc.add(station.name)
    print("Stations by River Cam:",sorted(stations_rc))
    for station in stations:
        if station.river == 'River Thames':
            stations_rt.add(station.name)
    print("Stations by River Thames:",sorted(stations_rt))


def rivers_by_station_number(stations, N):
    from floodsystem.stationdata import build_station_list
    stations = build_station_list()
    rivers_station_count = {}
    for station in stations:
        if station.river:
            rivers_station_count[station.river] = rivers_station_count.get(station.river, 0) + 1
    river_list = list(rivers_station_count.items())
    river_list.sort(key=lambda x: x[1], reverse=True)
    print((river_list)[:N])
    

def stations_by_distance(stations, p):
    radius = 6378
    
    

    #This function is supposed to calculate the distance between two points
    distances = []
    
    for station in stations:
        lat_1 = np.radians(p[0])
        lon_1 = np.radians(p[1])
        lat_2 = np.radians(station.coord[0])
        lon_2 = np.radians(station.coord[1])
        distance = 2 * radius * np.arcsin(np.sqrt(np.sin((lat_2 - lat_1) / 2)**2 + np.cos(lat_1) * np.cos(lat_2) * np.sin((lon_2 - lon_1) / 2)**2))
        distances.append((station, float(distance)))
    sorted_data = sorted_by_key(distances, 1)
    
    return sorted_data

def stations_within_radius(stations, centre, r):
    within = []
    radius = 6378
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