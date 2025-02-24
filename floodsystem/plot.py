import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    num_ticks = 10  # Number of x-ticks to display
    step = max(1, len(dates) // num_ticks)
    plt.xticks(dates[::step], rotation=45)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    low = station.typical_range[0]
    high = station.typical_range[1]
    plt.axhline(y = low, color = 'r', linestyle = '-')
    plt.axhline(y = high, color = 'g', linestyle = '-')
    plt.tight_layout()
    plt.show()

