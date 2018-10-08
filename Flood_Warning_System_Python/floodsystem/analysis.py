#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:55:33 2017

@author: admin
"""
import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    """ Takes a tuple of 'dates', tuple of 'levels' and integer 'p' 
        representing degrees of freedon as arguments. Returns 
        polynomial function and float offset"""
    
    x = matplotlib.dates.date2num(dates)
    d0 = x[0]
    
    p_coeff = np.polyfit(x-d0, levels, p)
    poly = np.poly1d(p_coeff)
    
    return poly, d0
    


def avgradient(levels):
    """ Takes a tuple 'levels' as an argument and returns sum of differences
        between consecutive elements starting with first element"""
    
    diff = []
    if levels != 0:
        for i in range(len(levels)-1):
            c = levels[i]-levels[i+1]
            diff.append(c)
        return round(sum(diff), 3)
    
    else:
        return 0
    
    

        
    
        
        
    
    