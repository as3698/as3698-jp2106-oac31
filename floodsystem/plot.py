import matplotlib.pyplot as plt
from floodsystem.utils import level_history
from floodsystem.stationdata import build_station_list
import matplotlib
from floodsystem.analysis import polyfit
import numpy as np


def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels, label='water level')
    num_ticks = 10  # Number of x-ticks to display
    step = max(1, len(dates) // num_ticks)
    plt.xticks(dates[::step], rotation=45)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    low = station.typical_range[0]
    high = station.typical_range[1]
    plt.axhline(y = low, color = 'r', linestyle = '-', label='Typical low')
    plt.axhline(y = high, color = 'g', linestyle = '-', label='Typical high')
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.show()



def plot_water_level_with_fit(station, old_dates, levels, p):
    dates = matplotlib.dates.date2num(old_dates)
    p_coeff = np.polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)
    plt.plot(old_dates, levels, '.', label='water level')
    num_ticks = 10  # Number of x-ticks to display
    step = max(1, len(old_dates) // num_ticks)
    plt.xticks(old_dates[::step], rotation=45)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    x1 = np.linspace(dates[0], dates[-1], len(old_dates))
    plt.plot(old_dates, poly(x1))
    low = station.typical_range[0]
    high = station.typical_range[1]
    plt.axhline(y = low, color = 'r', linestyle = '-', label='Typical low')
    plt.axhline(y = high, color = 'g', linestyle = '-', label='Typical high')
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.show()
    
    
'''
station = None
dates, levels = level_history("Bourton Dickler", 10)
dates_filtered = matplotlib.dates.date2num(dates)
degree = 4
poly, d0 = plot_water_level_with_fit(station, dates_filtered, levels, degree)
'''