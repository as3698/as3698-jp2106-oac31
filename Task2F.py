import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.utils import level_history



def polyfit(dates, levels, p):
    #p_coeff = np.polyfit(dates - dates[0], levels, p)
    print(dates)
    subtractor = dates[0]
    for i in range (len(dates)):
        dates[i] = dates[i] - subtractor
    print(dates)
    p_coeff = np.polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)
    plt.plot(dates, levels, '.')
    x1 = np.linspace(dates[0], dates[-1], 30)
    plt.plot(x1, poly(x1 - dates[0]))
    #plt.plot(x1, poly(x1))
    plt.show()
    d0 = dates[0]
    return poly, d0



dates, levels = level_history("Bourton Dickler", 2)
dates_filtered = matplotlib.dates.date2num(dates)
degree = 3
poly, d0 = polyfit(dates_filtered, levels, degree)





