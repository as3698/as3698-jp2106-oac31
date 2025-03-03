import matplotlib.pyplot as plt
from floodsystem.utils import level_history
from floodsystem.stationdata import build_station_list
import matplotlib
from floodsystem.analysis import polyfit
import numpy as np

#Used for task 2E, plots the water levels of a station over time
def plot_water_levels(station, dates, levels, test=False):
    if len(dates) != len(levels) or None in levels or None in dates:
        return('Data Corrupted')
    else:
        for i in range (5):
            try:
                plt.plot(dates, levels, label='water level')
                break
            except:
                pass
        num_ticks = 10  # Number of x-ticks to display
        step = max(1, len(dates) // num_ticks)
        plt.xticks(dates[::step], rotation=45)
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45)
        plt.title(station.name)
        low = station.typical_range[0]
        high = station.typical_range[1]
        plt.axhline(y = low, color = 'r', linestyle = '-', label='Typical low')
        plt.axhline(y = high, color = 'g', linestyle = '-', label='Typical high')
        plt.legend(loc="upper right")
        plt.tight_layout()
        if test == True:
            plt.close('all')
            plt.pause(0.1)
        plt.show()
        return('Data Plotted')

#Used for task 2F, plots the water levels of a station over time with a polynomial fit
def plot_water_level_with_fit(station, old_dates, levels, p, test=False):
    if len(old_dates) != len(levels) or None in levels or None in old_dates:
        return('Data Corrupted')
    else:
        dates = matplotlib.dates.date2num(old_dates)
        subtractor = dates[0]
        p_coeff = np.polyfit(dates - subtractor, levels, p)
        poly = np.poly1d(p_coeff)
        for i in range (5):
            try:
                plt.plot(old_dates, levels, '.', label='water level')
                break
            except:
                pass
        num_ticks = 10  # Number of x-ticks to display
        step = max(1, len(old_dates) // num_ticks)
        plt.xticks(old_dates[::step], rotation=45)
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.title(station.name)
        x1 = np.linspace(dates[0], dates[-1], len(old_dates))
        plt.plot(old_dates, poly(x1 - subtractor), label='polyfit')
        low = station.typical_range[0]
        high = station.typical_range[1]
        plt.axhline(y = low, color = 'r', linestyle = '-', label='Typical low')
        plt.axhline(y = high, color = 'g', linestyle = '-', label='Typical high')
        plt.legend(loc="upper right")
        plt.tight_layout()
        if test == True:
            plt.close('all')
            plt.pause(0.1)
        plt.show()
        return('Data Plotted')
    
    
'''
station = None
dates, levels = level_history("Bourton Dickler", 10)
dates_filtered = matplotlib.dates.date2num(dates)
degree = 4
poly, d0 = plot_water_level_with_fit(station, dates_filtered, levels, degree)
'''