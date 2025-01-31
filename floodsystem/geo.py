# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#from .utils import sorted_by_key  # noqa

#Uses geo.rivers_with_station to print how many rivers have at least one monitoring station (Representative result: 843) and prints the first 10 of these rivers in alphabetical order. Representative output:





#from floodsystem.stationdata import build_station_list


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
    print(sorted(stations_ra))
    for station in stations:
        if station.river == 'River Cam':
            stations_rc.add(station.name)
    print(sorted(stations_rc))
    for station in stations:
        if station.river == 'River Thames':
            stations_rt.add(station.name)
    print(sorted(stations_rt))


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
    




    
    








    



