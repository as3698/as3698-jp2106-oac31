from floodsystem.station import MonitoringStation
def List_of_stations():
    S1 = MonitoringStation(label = 's1', station_id = 'http://environment.data.gov.uk', measure_id = 'http://environment.data.gov.uk', coord = (1, 2), typical_range = (1, 2),
                 river = 'river1', town = 'town1')
    S2 = MonitoringStation(label = 's2', station_id = 'http://environment.data.gov.uk', measure_id = 'http://environment.data.gov.uk', coord = (2, 3), typical_range = (2,1),
                 river = 'river2', town = 'town2')
    S3 = MonitoringStation(label = 's3', station_id = 'http://environment.data.gov.uk', measure_id = 'http://environment.data.gov.uk', coord = (3, 4), typical_range = None,
                 river = 'river3', town = 'town3')
    S4 = MonitoringStation(label = 's4', station_id = 'http://environment.data.gov.uk', measure_id = 'http://environment.data.gov.uk', coord = (4, 5), typical_range = (4,5),
                 river = 'river4', town = 'town4')
    S5 = MonitoringStation(label = 's5', station_id = 'http://environment.data.gov.uk', measure_id = 'http://environment.data.gov.uk', coord = (5, 6), typical_range = (5,6),
                 river = 'river5', town = 'town5')
    return(S1,S2,S3,S4,S5)