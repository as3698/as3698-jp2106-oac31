from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
import pytest
from Olivers_Fantastic_Dataset import List_of_stations

def test_1e():
    output = rivers_by_station_number(List_of_stations(),1)
    assert output == [('river1', 1)]
test_1e