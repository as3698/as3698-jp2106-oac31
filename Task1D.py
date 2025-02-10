from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

def run():
    rivers_station = rivers_with_station(build_station_list())
    print(str(len(rivers_station)) + ' stations. First 10 - ' + str(sorted(rivers_station)[:10]))
    print('')

    rivers = stations_by_river(build_station_list())
    print('River Aire: ' + str(sorted(rivers['River Aire'])))
    print('River Cam: ' + str(sorted(rivers['River Cam'])))
    print('River Thames: ' + str(sorted(rivers['River Thames'])))
if __name__ == '__main__':
    run()