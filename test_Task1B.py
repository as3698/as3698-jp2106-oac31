from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from Task1B import closest_stations
def test_stations_by_distance():
    coordinate = (52.2053, 0.1218)
    final = closest_stations(coordinate)

    #output = stations_by_distance(build_station_list(), coordinate)

    #final = [(station[0].name, station[0].town, station[1]) for station in output]

    #print(final[:10])
    #print(final[-10:])

    assert final[:10] == [('Cambridge Jesus Lock', 'Cambridge', 0.84), ('Bin Brook', 'Cambridge', 2.5), ("Cambridge Byron's Pool", 'Grantchester', 4.07), ('Cambridge Baits Bite', 'Milton', 5.12), ('Girton', 'Girton', 5.23), ('Haslingfield Burnt Mill', 'Haslingfield', 7.04), ('Oakington', 'Oakington', 7.13), ('Stapleford', 'Stapleford', 7.27), ('Comberton', 'Comberton', 7.74), ('Dernford', 'Great Shelford', 7.99)]
    assert final[-10:] == [('Gwithian', 'Gwithian', 442.06), ('Helston County Bridge', 'Helston', 443.38), ('Loe Pool', 'Helston', 445.07), ('Relubbus', 'Relubbus', 448.65), ('St Erth', 'St Erth', 449.03), ('St Ives Consols Farm', 'St Ives', 450.07), ('Penzance Tesco', 'Penzance', 456.39), ('Penzance Alverton', 'Penzance', 458.58), ('Newlyn Coombe', 'Newlyn', 459.11), ('Penberth', 'Penberth', 467.53)]