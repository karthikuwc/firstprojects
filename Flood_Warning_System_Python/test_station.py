"""Unit test for the station module"""

import pytest
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

# Test if incosistent function works
def test_inconsistenttypicalrangestations():
    
    stations = [MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test",
                                  coord=(52.2053,
                                         0.1218),
                                  typical_range= (0.0, 1),
                                  river=None,
                                  town=None), 
                MonitoringStation(station_id= None,
                                  measure_id=None,
                                  label= "test2",
                                  coord=(1.0,
                                         0.0),
                                  typical_range= (1,0.0),
                                  river=None,
                                  town=None)]
                                         
    inconsistent = inconsistent_typical_range_stations(stations)
    
    assert inconsistent == ["test","test2"]
    
    
    
    
