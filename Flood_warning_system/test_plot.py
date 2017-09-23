#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:15:51 2017

@author: admin
"""

from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.station import MonitoringStation
import datetime

def test_plotwaterlevels():
    
    station = MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test",
                                  coord=(52.2053,
                                         0.1218),
                                  typical_range=(0.25,1.25),
                                  river=None,
                                  town=None)
                                  
    dates = [datetime.datetime(2017, 2, 25, 4, 0), 
             datetime.datetime(2017, 2, 25, 3, 45), 
             datetime.datetime(2017, 2, 25, 3, 30),
             datetime.datetime(2017, 2, 25, 3, 15), 
             datetime.datetime(2017, 2, 25, 3, 0), 
             datetime.datetime(2017, 2, 25, 2, 45),
             datetime.datetime(2017, 2, 25, 2, 30),
             datetime.datetime(2017, 2, 25, 2, 15)]
    
    levels = [0.75]*len(dates)
    
    plot_water_levels(station, dates, levels)
    
test_plotwaterlevels()

def test_plotwaterlevelwithfit():
    
    station = MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test",
                                  coord=(52.2053,
                                         0.1218),
                                  typical_range=(0.25,1.25),
                                  river=None,
                                  town=None)
                                  
    dates = [datetime.datetime(2017, 2, 25, 4, 0), 
             datetime.datetime(2017, 2, 25, 3, 45), 
             datetime.datetime(2017, 2, 25, 3, 30),
             datetime.datetime(2017, 2, 25, 3, 15), 
             datetime.datetime(2017, 2, 25, 3, 0), 
             datetime.datetime(2017, 2, 25, 2, 45),
             datetime.datetime(2017, 2, 25, 2, 30),
             datetime.datetime(2017, 2, 25, 2, 15)]
    
    levels = [0.75]*len(dates)
    
    plot_water_level_with_fit(station, dates, levels, 3)
    
test_plotwaterlevelwithfit()