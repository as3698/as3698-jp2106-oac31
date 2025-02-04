from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    print(sorted(inconsistent_stations))

if __name__ == "__main__":
    run()