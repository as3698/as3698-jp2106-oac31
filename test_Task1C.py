from floodsystem.stationdata import build_station_list
from Task1C import task_1C
from List_of_stations import List_of_stations


def test_task_1C():
    r = 10
    centre = (52.2053, 0.1218)
    out = task_1C(build_station_list(), centre, r)
    #stations = build_station_list()

    #output_c = stations_within_radius(stations, centre, r)


    #final = [(station[0].name) for station in output_c]
    #final.sort()
    assert out == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']

def test_task_1C_2():
    r = 10
    centre = (51.5104, 0.1419)
    out = task_1C(build_station_list(), centre, r)
    assert out == ['Collier Row', 'Crayford', 'Gaynes Park', 'Hall Place', 'Hornchurch_Bretons Farm', 'Lamorbey Park', 'Romford', 'Seven Kings Park']

def test_task_1C_3():
    r = 200
    centre = (3,4)
    out = task_1C(List_of_stations(), centre, r)
    assert out == ['s2', 's3', 's4']

def test_task_1C_3():
    r = 2
    centre = (3,4)
    out = task_1C(List_of_stations(), centre, r)
    assert out == ['s3']

