import matplotlib.pyplot as plt
from Olivers_Fantastic_Dataset import List_of_stations
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit





def test_plot_water_levels_1():
    dates = [1,2,3,4,5]
    levels = dates
    stations = List_of_stations()
    station = stations[0]
    output = plot_water_levels(station, dates, levels)
    #print(output)
    assert output == 'Data Plotted'


def test_plot_water_levels_2():
    dates = [1,2,3,4,5,6]
    levels = [1,2,3,4,5]
    stations = List_of_stations()
    station = stations[0]
    output =  plot_water_levels(station, dates, levels)
    #print(output)
    assert output == 'Data Corrupted'

def test_plot_water_levels_3():
    dates = [1,2,3,4,5,6]
    levels = [1,2,3,4,5,None]
    stations = List_of_stations()
    station = stations[0]
    output =  plot_water_levels(station, dates, levels)
    #print(output)
    assert output == 'Data Corrupted'

def test_plot_water_level_with_fit_1():
    dates = [1,2,3,4,5]
    levels = dates
    stations = List_of_stations()
    station = stations[0]
    p = 4
    output = plot_water_level_with_fit(station, dates, levels, 2)
    #print(output)
    assert output == 'Data Plotted'

def test_plot_water_level_with_fit_2():
    dates = [1,2,3,4,5,6]
    levels = [1,2,3,4,5]
    stations = List_of_stations()
    station = stations[0]
    p = 4
    output = plot_water_level_with_fit(station, dates, levels, 2)
    #print(output)
    assert output == 'Data Corrupted'

def test_plot_water_level_with_fit_3():
    dates = [1,2,3,4,5,6]
    levels = [1,2,3,4,5,None]
    stations = List_of_stations()
    station = stations[0]
    p = 4
    output = plot_water_level_with_fit(station, dates, levels, 2)
    #print(output)
    assert output == 'Data Corrupted'

#test_plot_water_levels_1()
#test_plot_water_levels_2()
#test_plot_water_levels_3()
#test_plot_water_level_with_fit_1()
#test_plot_water_level_with_fit_2()
#test_plot_water_level_with_fit_3()