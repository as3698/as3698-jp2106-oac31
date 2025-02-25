import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.utils import level_history

def polyfit(old_dates, levels, p):
    dates = matplotlib.dates.date2num(old_dates)
    p_coeff = np.polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)
    d0 = dates[0]
    return poly, d0

old_dates = [1,2,3,4,5]
levels = old_dates
