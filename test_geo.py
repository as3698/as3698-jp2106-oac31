from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from List_of_stations import List_of_stations
'''
def test_geo_radius():
    stations = build_station_list()

    output_geo = stations_within_radius(stations, centre, r)


    out_Buckingham = [(station[0].name) for station in output_geo]
    out_Buckingham.sort()
    assert out_Buckingham == ['Collier Row', 'Crayford', 'Gaynes Park', 'Hall Place', 'Hornchurch_Bretons Farm', 'Lamorbey Park', 'Romford', 'Seven Kings Park']
'''


def geo_radius_2():
    centre = (3,4)
    radius = 5
    output_geo = stations_within_radius(List_of_stations(), centre, radius)
    station_names = [station[0].name for station in output_geo]
    assert station_names == ['s3']



'''
def test_geo_distance():
    output = stations_by_distance(build_station_list(), coordinate)
    final = [(station[0].name, station[0].town, round(station[1], 2)) for station in output]
    assert final[:10] == [('Hornchurch_Bretons Farm', 'Elm Park', 4.96), ('Crayford', 'Crayford', 7.02), ('Hall Place', 'Coldblow', 7.25), ('Seven Kings Park', 'Seven Kings', 7.34), ('Lamorbey Park', 'Sidcup', 8.05), ('Gaynes Park', 'Upminster', 8.1), ('Romford', 'Romford', 8.43), ('Collier Row', 'Romford', 9.76), ('Redbridge', 'Wanstead', 10.13), ('Manor House Gardens', 'Hither Green', 11.2)]
    assert final[-10:] == [('Coldgate Mill', 'North Middleton', 467.59), ('Wooler', 'Wooler', 470.73), ('Weetwood Bridge', 'Weetwood Bridge', 471.3), ('Waren Mill', 'Warenmill', 472.15), ('Belford', 'Belford', 472.78), ('Doddington Bridge', 'Doddington Bridge', 473.13), ('Pawston', 'Pawston', 480.29), ('Sprouston', 'Sprouston', 485.73), ('Heaton Mill', 'Heaton Mill', 487.29), ('Norham', 'Norham', 492.34)]
'''
def test_geo_distance_2():
    center = (3,4)
    stations = List_of_stations()
    output = stations_by_distance(stations, center)
    station_names = [station[0].name for station in output]
    assert station_names == ['s3', 's4', 's2', 's5', 's1']


