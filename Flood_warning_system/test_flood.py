#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:14:26 2017

@author: admin
"""

from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

def test_stationsleveloverthreshold():
    
    stations = [MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test",
                                  coord=(52.2053,
                                         0.1218),
                                  typical_range=(0,1),
                                  river=None,
                                  town=None), 
                MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test2",
                                  coord=(1.0,
                                         0.0),
                                  typical_range=(0,1),
                                  river=None,
                                  town=None), 
                MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test2",
                                  coord=(1.0,
                                         0.0),
                                  typical_range=(0,1),
                                  river=None,
                                  town=None)]
    
    stations[0].latest_level = 0.9
    stations[1].latest_level = 1.0
    stations[2].latest_level = 0.7
    
    assert stations_level_over_threshold(stations, 0.8) == [("test2",1.0),("test",0.9)]

def test_stationshighestrellevel():
    
    stations = [MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test",
                                  coord=(52.2053,
                                         0.1218),
                                  typical_range=(0,1),
                                  river=None,
                                  town=None), 
                MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test2",
                                  coord=(1.0,
                                         0.0),
                                  typical_range=(0,1),
                                  river=None,
                                  town=None), 
                MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test2",
                                  coord=(1.0,
                                         0.0),
                                  typical_range=(0,1),
                                  river=None,
                                  town=None)]
    
    stations[0].latest_level = 0.9
    stations[1].latest_level = 1.0
    stations[2].latest_level = 0.7
    
    assert stations_highest_rel_level(stations, 1) == [("test2",1.0)]

test_stationsleveloverthreshold()
test_stationshighestrellevel()
                
    

    
        
    
    

