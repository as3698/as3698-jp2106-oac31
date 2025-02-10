from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
import numpy as np



#Test section where I tested the Wikipedia formula
radius = 6378


#distance = 2*radius*np.arcsin(np.sqrt(0.5*(1-np.cos(lat)+(np.cos(lat_1))*(np.cos(lat_2)*(1-np.cos(lon))))))


#The two functions create two lists, one of names and one of coordinates
def get_station_names():
    station_names = [station.name for station in build_station_list()]
    return station_names

def get_station_coord():
    station_coord = [station.coord for station in build_station_list()]
    return station_coord 


#Creates a multi-dimensional list of the names and coordinates
duo_list = list(map(list,zip(get_station_names(), get_station_coord()))) 


#WORK HERE
#This function is supposed to calculate the distance between two points
distances = []
num = 0
def get_station_distance():
    for name, coord in duo_list:
        lat_1 = np.radians(52.2053)
        lon_1 = np.radians(0.1218)
        lat_2 = np.radians(coord[num])
        lon_2 = np.radians(coord[num+1])
        distance = 2 * radius * np.arcsin(np.sqrt(np.sin((lat_2 - lat_1) / 2)**2 + np.cos(lat_1) * np.cos(lat_2) * np.sin((lon_2 - lon_1) / 2)**2))
        distances.append(station, distance)
    sorted_data = sorted(distances, key=lambda x: x[1])
    return sorted_data



#Creates a multi-dimensional list of the names and coordinates
tri_list = list(map(list,zip(get_station_names(), get_station_coord(), get_station_distance())))   

sorted_data = sorted(tri_list, key=lambda x: x[2])


list_of_tuples = list(map(tuple, sorted_data))
cleaned_data = [(name, coords, float(dist)) for name, coords, dist in list_of_tuples]












-------------


#from .utils import sorted_by_key  # noqa
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
import numpy as np

def stations_by_distance(stations, p):
    radius = 6378
    
    def get_station_names():
        station_names = [station.name for station in stations]
        return station_names
    
    def get_station_coord():
        station_coord = [station.coord for station in stations]
        return station_coord 

    #Creates a multi-dimensional list of the names and coordinates
    duo_list = list(map(list,zip(get_station_names(), get_station_coord()))) 

    #This function is supposed to calculate the distance between two points
    distances = []
    def get_station_distance():
        for station in stations:
            lat_1 = np.radians(p[0])
            lon_1 = np.radians(p[1])
            lat_2 = np.radians(station.coord[0])
            lon_2 = np.radians(station.coord[1])
            distance = 2 * radius * np.arcsin(np.sqrt(np.sin((lat_2 - lat_1) / 2)**2 + np.cos(lat_1) * np.cos(lat_2) * np.sin((lon_2 - lon_1) / 2)**2))
            distances.append((station, distance))
        sorted_data = sorted(distances, key=lambda x: x[1])
        return sorted_data



    #Creates a multi-dimensional list of the names and coordinates
    tri_list = list(map(list,zip(stations, get_station_distance())))   

    sorted_data = sorted(distances, key=lambda x: x[1])


    #list_of_tuples = list(map(tuple, sorted_data))
    #Removes np.float64
    #cleaned_data = [(name, float(dist)) for name, dist in list_of_tuples]
    return sorted_data
    




    # python3 -m floodsystem.geo






# python3 -m floodsystem.geo