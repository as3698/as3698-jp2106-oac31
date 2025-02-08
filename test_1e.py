from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
import pytest

def test_1e():
    output = rivers_by_station_number(build_station_list)
    assert output == [('River Thames', 55), ('River Avon', 32), ('River Great Ouse', 30), ('River Derwent', 26), ('River Aire', 24), ('River Calder', 23), ('River Severn', 21), ('River Stour', 20), ('River Colne', 19)]

test_1e