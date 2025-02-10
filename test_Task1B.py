from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from Task1B import closest_stations
from List_of_stations import List_of_stations


def test_stations_by_distance():
    coordinate = (52.2053, 0.1218)
    final = closest_stations(build_station_list(), coordinate)

    #output = stations_by_distance(build_station_list(), coordinate)

    #final = [(station[0].name, station[0].town, station[1]) for station in output]

    #print(final[:10])
    #print(final[-10:])

    assert final[:10] == [('Cambridge Jesus Lock', 'Cambridge', 0.84), ('Bin Brook', 'Cambridge', 2.5), ("Cambridge Byron's Pool", 'Grantchester', 4.07), ('Cambridge Baits Bite', 'Milton', 5.12), ('Girton', 'Girton', 5.23), ('Haslingfield Burnt Mill', 'Haslingfield', 7.04), ('Oakington', 'Oakington', 7.13), ('Stapleford', 'Stapleford', 7.27), ('Comberton', 'Comberton', 7.74), ('Dernford', 'Great Shelford', 7.99)]
    assert final[-10:] == [('Gwithian', 'Gwithian', 442.06), ('Helston County Bridge', 'Helston', 443.38), ('Loe Pool', 'Helston', 445.07), ('Relubbus', 'Relubbus', 448.65), ('St Erth', 'St Erth', 449.03), ('St Ives Consols Farm', 'St Ives', 450.07), ('Penzance Tesco', 'Penzance', 456.39), ('Penzance Alverton', 'Penzance', 458.58), ('Newlyn Coombe', 'Newlyn', 459.11), ('Penberth', 'Penberth', 467.53)]

def test_stations_by_distance_2():
    coordinate = (51.5014, 0.1419)
    final = closest_stations(build_station_list(), coordinate)
    assert final[:10] == [('Hornchurch_Bretons Farm', 'Elm Park', 5.8), ('Crayford', 'Crayford', 6.07), ('Hall Place', 'Coldblow', 6.27), ('Lamorbey Park', 'Sidcup', 7.09), ('Seven Kings Park', 'Seven Kings', 8.29), ('Gaynes Park', 'Upminster', 8.72), ('Romford', 'Romford', 9.4), ('Hawley', 'Hawley', 10.59), ('Manor House Gardens', 'Hither Green', 10.69), ('Collier Row', 'Romford', 10.76)]
    assert final[-10:] == [('Coldgate Mill', 'North Middleton', 468.54), ('Wooler', 'Wooler', 471.69), ('Weetwood Bridge', 'Weetwood Bridge', 472.26), ('Waren Mill', 'Warenmill', 473.12), ('Belford', 'Belford', 473.75), ('Doddington Bridge', 'Doddington Bridge', 474.09), ('Pawston', 'Pawston', 481.24), ('Sprouston', 'Sprouston', 486.67), ('Heaton Mill', 'Heaton Mill', 488.25), ('Norham', 'Norham', 493.3)]

def test_stations_by_distance_3():

    coordinate = (51.5014, 0.1419)

    final = closest_stations(List_of_stations(), coordinate)
    assert final == [('s5', 'town5', 5199.11), ('s4', 'town4', 5301.17), ('s3', 'town3', 5405.09), ('s2', 'town2', 5510.79), ('s1', 'town1', 5618.21)]



