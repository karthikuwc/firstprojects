#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 17:16:49 2017

@author: admin
"""
import pytest
from floodsystem.geo import station_by_distance
from floodsystem.station import MonitoringStation
from geopy.distance import great_circle
from floodsystem.geo import stations_within_radius
from floodsystem.geo import search_station
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

# Test if station distance function returns correct values given
# test argument

def test_distance():
    test = MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test",
                                  coord=(50.0,
                                         0.0),
                                  typical_range=None,
                                  river=None,
                                  town=None)
                                  
    testl = []
    testl.append(test)
    
    sd = station_by_distance(testl, (52.2053, 0.1218))
    d = round(1.60934*great_circle((52.2053, 0.1218),(50.0, 0.0)).miles, 4)
    
    assert type(sd[0]) == tuple
    assert sd[0][0] == "test"
    assert sd[0][1] == d

# Test if function correctly returns stations within given radius

def test_stationswithinradius():
    
    stations = [MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test",
                                  coord=(52.2053,
                                         0.1218),
                                  typical_range=None,
                                  river=None,
                                  town=None), 
                MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test2",
                                  coord=(1.0,
                                         0.0),
                                  typical_range=None,
                                  river=None,
                                  town=None)]
                                         
    origincoord = (52.2053, 0.1218)
    withinrad = stations_within_radius(stations, origincoord, 10)
    
    namls = []

    for station in withinrad:
        namls.append(station.name)
    
    assert namls == ['test']

# Test if function correctly returns all rivers

def test_riverswithstation():
    
    stations = [MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label=None,
                                  coord=(52.2053,
                                         0.1218),
                                  typical_range=None,
                                  river="test2",
                                  town=None), 
                MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= None,
                                  coord=(1.0,
                                         0.0),
                                  typical_range=None,
                                  river="test",
                                  town=None)]
                                         
    rivers = rivers_with_station(stations)
    
    assert rivers == ["test","test2"]

# Test if function correctly returns stations by a particular river
    
def test_stationsbyriver():
    
    stations = [MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label="test2",
                                  coord=(52.2053,
                                         0.1218),
                                  typical_range=None,
                                  river="test",
                                  town=None), 
                MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test",
                                  coord=(1.0,
                                         0.0),
                                  typical_range=None,
                                  river="test",
                                  town=None)]
    
    riverstationmap = stations_by_river(stations)
    
    assert riverstationmap["test"] == ["test","test2"]

# Test if function correctly returns station when given name
    
def test_searchstation():
    
    stations = [MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label="test2",
                                  coord=(52.2053,
                                         0.1218),
                                  typical_range=None,
                                  river="test",
                                  town=None), 
                MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test",
                                  coord=(1.0,
                                         0.0),
                                  typical_range=None,
                                  river="test",
                                  town=None)]

    station = search_station(stations, "test")

    assert station == stations[1]

# Test if function correctly returns rivers with greatest number of stations
def test_riversbystationnumber():
    
    stations = [MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label="test2",
                                  coord=(52.2053,
                                         0.1218),
                                  typical_range=None,
                                  river="test",
                                  town=None), 
                MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test",
                                  coord=(1.0,
                                         0.0),
                                  typical_range=None,
                                  river="test",
                                  town=None), 
                MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test3",
                                  coord=(1.0,
                                         0.0),
                                  typical_range=None,
                                  river="test2",
                                  town=None)]
                                         
    N = 1
    M = 2
    rivstatno = rivers_by_station_number(stations, N)
    rivstatno1 = rivers_by_station_number(stations, M)
    
    assert rivstatno == [('test',2)]
    assert rivstatno1 == [('test',2),('test2',1)]
    

test_stationswithinradius()
test_distance()
test_riverswithstation()
test_stationsbyriver()
test_searchstation()

    