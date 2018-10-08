"""This module contains a collection of functions related to
geographical data.

"""





from .utils1 import sorted_by_key
from geopy.distance import great_circle



def search_station(stations, name):
    """A function that returns a station referenced by name"""
    
    for station in stations:
        if station.name == name:
            return station
            

def station_by_distance(stations, p):
    """A function that takes a list of MonitoringStations and a co-ordinate, and
    returns a list of tuples: (station, distance)"""
    sd = []
    for station in stations:
        s = (station.name, round(1.60934*great_circle(station.coord, p).miles,
                                 4))
        sd.append(s)
    
    sd = sorted_by_key(sd,1)
    return sd


def stations_within_radius(stations, centre, r):
    """A function that returns all the stations within a particular radius
    of a coordinate."""

    
    disls = station_by_distance(stations, centre)
    
    radls = []
    
    for station in disls:
        if station[1] <= r:
            radls.append(search_station(stations, station[0]))
            
    return radls



def rivers_with_station(stations):
    """A function that returns all the rivers which have monitoring stations"""
    
    rivers = []
    
    for station in stations:
        rivers.append(station.river)
    
    river = sorted(set(rivers))
        
    return river
    


def stations_by_river(stations):
    """A function that shows all the stations by a particular river"""

    riverstationmap = {}
    for station in stations:
        if station.river not in riverstationmap:
            riverstationmap[station.river] = [station.name]
        else:
            s = station.name
            riverstationmap[station.river].append(s)
    
    for river in riverstationmap:
        riverstationmap[river] = sorted(riverstationmap[river])

    return riverstationmap

    

def rivers_by_station_number(stations, N):
    """A function that returns the N rivers with the greatest number of monitoring
    stations."""
    
    riverstationmap = stations_by_river(stations)
    rivstatno = []

    for river in riverstationmap:
        rivstatno.append((river, len(riverstationmap[river])))
        
    rivstatno = sorted_by_key(rivstatno,1)
    rivstatno.reverse()
    
    i = N - 1
    
    while rivstatno[i][1] == rivstatno[i+1][1]:
        
        i += 1
    
    return rivstatno[:i+1]




