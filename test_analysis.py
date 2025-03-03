import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.utils import level_history
from floodsystem.analysis import polyfit


def test_polyfit_1():
    old_dates = [1,2,3,4,5]
    levels = old_dates
    test = []
    output = polyfit(old_dates, levels, 2)
    output = list(output)
    for i in range (0,4):
        thing = output[0]
        item = ((thing))[i]
        item = round(item, 4)
        item = int(item)
        test.append(item)
    output[1] = round(output[1], 4)
    #print(test, d0)
    assert test == [0, 86400000000, 326443, 0] and output[1] == 0.0
    

def test_polyfit_2():
    old_dates = [1,2,3,4,5]
    levels = [1,2,3,4]
    test = []
    output = polyfit(old_dates, levels, 2)
    output = list(output)
    for i in range (0,4):
        thing = output[0]
        item = ((thing))[i]
        item = round(item, 3)
        item = int(item)
        test.append(item)
    output[1] = round(output[1], 4)
    #print(test, d0)
    assert test == [0, 86400000000, -610998, 0] and output[1] == 0.0