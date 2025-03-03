import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.utils import level_history

def polyfit(old_dates, levels, p):
    if len(old_dates) != len(levels):
        difference = len(old_dates) - len(levels)
        if difference > 0:
            old_dates = old_dates[:-difference]
        else:
            levels = levels[:-difference]
    for i in range (0,len(old_dates)):
        if levels[i] == None or old_dates[i] == None:
            del old_dates[i]
            del levels[i]
    dates = matplotlib.dates.date2num(old_dates)
    p_coeff = np.polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)
    d0 = dates[0]
    output = (poly, d0)
    return output



#dates, levels = level_history("Bourton Dickler", 10)

#degree = 6
#poly, d0 = polyfit(dates, levels, degree)
#print(poly)
#print(d0)

