def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    num_ticks = 10  # Number of x-ticks to display
    step = max(1, len(dates) // num_ticks)
    plt.xticks(dates[::step], rotation=45)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station)
    plt.axhline(y = 0.5, color = 'r', linestyle = '-')
    plt.tight_layout()
    plt.show()

plot_water_levels(station, dates, levels)