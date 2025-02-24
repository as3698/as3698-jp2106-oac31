from floodsystem.stationdata import build_station_list
import pytest
from Olivers_Fantastic_Dataset import List_of_stations
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold 
from floodsystem.stationdata import update_water_levels


def test_2b():
    stations = List_of_stations()
    test_output = stations_level_over_threshold(stations, 0.8)
    assert test_output == [('s1', 19.0), ('s4', 16.0), ('s5', 15.0)]
