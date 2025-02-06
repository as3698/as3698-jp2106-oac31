from tkinter.filedialog import test
from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.geo import 


rivers_with_station(build_station_list)

stations_by_river(build_station_list)

def test_d1():
    output = rivers_with_station(build_station_list)
    assert output == 'Number of rivers with at least one monitoring station: 1052['Addlestone Bourne', 'Aire Washlands', 'Alconbury Brook', 'Aldingbourne Rife', 'Aller Brook', 'Allison Dyke', 'Alphin Brook', 'Alverthorpe Beck', 'Ampney Brook', 'Amwell Loop']