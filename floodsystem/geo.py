# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#from .utils import sorted_by_key  # noqa
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
import numpy as np

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
    sorted_data = sorted(distances, key=lambda x: x[1])
    
    return sorted_data



   
    




    # python3 -m floodsystem.geo