# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#from .utils import sorted_by_key  # noqa

import numpy as np
from .utils import sorted_by_key
from haversine import haversine

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
        cam = (lat_1, lon_1)
        place = (lat_2, lon_2)
        distance_c = haversine(cam, place)
        #distance_c = 2 * radius * np.arcsin(np.sqrt(np.sin((lat_2 - lat_1) / 2)**2 + np.cos(lat_1) * np.cos(lat_2) * np.sin((lon_2 - lon_1) / 2)**2))
        if distance_c <= r:
            within.append((station, float(distance_c)))
    return within
    



   
    




    # python3 -m floodsystem.geo