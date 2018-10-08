#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:41:46 2017

@author: admin
"""
from .analysis import polyfit
import matplotlib
import matplotlib.pyplot as plt





def plot_water_levels(station, dates, levels):
    """ Takes a 'station' Type(MonitoringStation), array of values corresponding
        to equally spaced datetime values between desired interval, and array
        of measurements of water levels (same length as dates) to return plot
        of datetime vs measured levels, typical high, typical low"""
        
    tlow = [station.typical_range[0]]*len(dates)
    thigh = [station.typical_range[1]]*len(dates)
    plt.plot(dates, levels, label = 'Latest Levels')
    plt.plot(dates, tlow, label = 'Typical Low')
    plt.plot(dates, thigh, label = 'Typical High')
    plt.xlabel('Date')
    plt.ylabel('Water Level')
    plt.xticks(rotation = 45);
    plt.title("Station: {}".format(station.name))
    plt.legend()
    plt.tight_layout()
    plt.show()
    

def plot_water_level_with_fit(station, dates, levels, p):
    
    """ Takes a 'station' Type(MonitoringStation), array of values corresponding
    to equally spaced datetime values between desired interval, and array
    of measurements of water levels (same length as dates), and degrees of 
    freedom 'p' of best fit polynomial; to return plot
    of datetime vs measured levels, typical high, typical low, bestfit 
    polynomial"""
    x = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(dates, levels, p)
    tlow = [station.typical_range[0]]*len(dates)
    thigh = [station.typical_range[1]]*len(dates)
    plt.plot(dates, levels, label = 'Latest Levels')
    plt.plot(dates, tlow, label = 'Typical Low')
    plt.plot(dates, thigh, label = 'Typical High')
    plt.plot(dates, poly(x-d0), label = 'Best Fit')
    plt.xlabel('Date')
    plt.ylabel('Water Level')
    plt.xticks(rotation = 45);
    plt.title("Station: {}".format(station.name))
    plt.legend()
    plt.tight_layout()
    plt.show()
    