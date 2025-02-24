import matplotlib.pyplot as plt
from floodsystem.utils import level_history
from floodsystem.stationdata import build_station_list
import matplotlib
from floodsystem.analysis import polyfit


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
    plt.plot(dates, levels)
    num_ticks = 10  # Number of x-ticks to display
    step = max(1, len(dates) // num_ticks)
    plt.xticks(dates[::step], rotation=45)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    days = 2
    dates, levels = level_history(station.name, days)
    dates_filtered = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(dates_filtered, levels, p)
    plt.plot(dates, poly)
    plt.tight_layout()
    plt.show()

stations = build_station_list()
station = stations[0]
dates, levels = level_history(station.name, 10)
p = 3

plot_water_level_with_fit(station, dates, levels, p)