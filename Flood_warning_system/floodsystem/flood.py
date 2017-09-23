#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 10:33:57 2017

@author: admin
"""
from .utils1 import sorted_by_key
from .station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    """ Argument 'stations' takes list of stations, and function
        returns list of tuples (station name, relative level) for 
        stations with relative level above argument 'tol'"""
    
    stationsoverthr = []

    for station in stations:
    
        if MonitoringStation.relative_water_level(station) != None:
            
            if MonitoringStation.relative_water_level(station) > tol:
                
                tup = (station.name, MonitoringStation.relative_water_level(station))
                
                stationsoverthr.append(tup)
                
            
    stationsoverthr = sorted_by_key(stationsoverthr, 1)
    stationsoverthr.reverse()
        
    return stationsoverthr


def stations_highest_rel_level(stations, N):
    """ Argument 'stations' takes list of stations, argument N
    specifies number of stations with highest relative water level
    you would like the function to return"""

    namelevel = stations_level_over_threshold(stations, -1000000)

    return namelevel[:N]


    
