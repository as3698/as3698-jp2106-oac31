# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""
import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels


def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple::

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple::

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

#Jaiden added to output the water levels of a station over the past input days
def level_history(station_name, dt):

    # Build list of stations
    stations = build_station_list()

    # Station name to find
    

    # Find station
    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break

    # Check that station could be found. Return if not found.
    if not station_cam:
        print("Station {} could not be found".format(station_name))
        return

    # Fetch data over past 2 days
    dates, levels = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    
    things = []
    things_2 = []

    # Print level history
    for date, level in zip(dates, levels):
        date = date.strftime("%Y-%m-%d %H:%M:%S")
        things.append((date))
        things_2.append((level))

    
    return things, things_2
    


#Jaiden added to output the current water levels of all stations
def current_level():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    things = []
    for station in stations:
      things.append((station.name, station.latest_level))
    return things
