from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def test_1f():
    #Test takes two locations, one known to have consistent data (Gaw Bridge), and one known to have inconsistent data (Braunton)
    #Test checks that only Braunton is returned from the inconsistent_typical_range_stations function
    stations = build_station_list()
    test_stations = []
    for station in stations:
        if station.name in ['Gaw Bridge', 'Braunton']:
            test_stations.append(station)
    assert(inconsistent_typical_range_stations(test_stations) == ['Braunton'])