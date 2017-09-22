#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:42:13 2017

@author: admin
"""

from floodsystem.analysis import avgradient
from floodsystem.analysis import polyfit
import numpy as np
import datetime

def test_avgradient():
    
    c = (1,1,1,1,1,1)
    
    assert avgradient(c) == 0

def test_polyfit():
    
    dates = [datetime.datetime(2017, 2, 27, 18, 0),
             datetime.datetime(2017, 2, 27, 17, 45), 
            datetime.datetime(2017, 2, 27, 17, 30), 
            datetime.datetime(2017, 2, 27, 17, 15)]
    
    levels = (1, 1, 1, 1)
    
    p = 3
    
    t , d = polyfit(dates, levels, p)
    i = [  6.27318682e-11,   2.57949080e-12,   1.02325416e-15,   1.00000000e+00]
    
    assert all(t.c) == all(i)
    assert d == 736387.75

test_avgradient()
test_polyfit()
    