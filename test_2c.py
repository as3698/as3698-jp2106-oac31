import pytest
from Olivers_Fantastic_Dataset import List_of_stations
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels


def test_2c():
    stations = List_of_stations()
    test_output = stations_highest_rel_level(stations, 2)
    assert test_output == [('s1', 19.0), ('s4', 16.0)]
    
