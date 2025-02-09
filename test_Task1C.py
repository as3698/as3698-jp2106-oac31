from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
import numpy as np
from Task1C import task_1C


def test_task_1C():
    r = 10
    centre = (52.2053, 0.1218)
    out = task_1C(centre, r)
    #stations = build_station_list()

    #output_c = stations_within_radius(stations, centre, r)


    #final = [(station[0].name) for station in output_c]
    #final.sort()
    assert out == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']