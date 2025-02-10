from Olivers_Fantastic_Dataset import List_of_stations
from floodsystem.station import inconsistent_typical_range_stations


def test_1f():
    stations = List_of_stations()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    assert('s2' in inconsistent_stations)
    assert('s3' in inconsistent_stations)
    assert(len(inconsistent_stations) == 2)