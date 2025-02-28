import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.utils import level_history
from floodsystem.analysis import polyfit


def test_polyfit_1():
    old_dates = [1,2,3,4,5]
    levels = old_dates
    test = []
    poly, d0 = polyfit(old_dates, levels, 2)
    for i in range (1,4):
        item = ((poly))[i]
        item = round(item, 4)
        item = int(item)
        test.append(item)
    assert test == [86400000000, -84878, 0]
    

def test_polyfit_2():
    old_dates = [1,2,3,4,5]
    levels = old_dates
    test = []
    poly, d0 = polyfit(old_dates, levels, 2)
    for i in range (1,4):
        item = ((poly))[i]
        item = round(item, 4)
        item = int(item)
        test.append(item)
    assert test == [86400000000, -84878, 0]



