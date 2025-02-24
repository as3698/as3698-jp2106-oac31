import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.utils import level_history
from floodsystem.stationdata import build_station_list

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

def plot_water_level_with_fit(station, dates, levels, p):
    
    num_ticks = 10  # Number of x-ticks to display
    step = max(1, len(dates) // num_ticks)
    plt.xticks(dates[::step], rotation=45)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    subtractor = dates[0]
    old_dates = dates
    for i in range (len(dates)):
        dates[i] = dates[i] - subtractor
    p_coeff = np.polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)
    plt.plot(old_dates, levels, label='water level')
    x1 = np.linspace(dates[0], dates[-1], 30)
    plt.plot(x1, poly(x1 - dates[0]))
    #plt.plot(x1, poly(x1))
    plt.show()
    d0 = dates[0]
    return poly, d0



dates, levels = level_history("Bourton Dickler", 2)
dates_filtered = matplotlib.dates.date2num(dates)
p = 3
station = build_station_list()[0]
poly, d0 = plot_water_level_with_fit(station, dates_filtered, levels, p)