"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d =  "  Station Name:     {}\n".format(self.name)
        d += "    Station ID:     {}\n".format(self.station_id)
        d += "Measurement ID:     {}\n".format(self.measure_id)
        d += "    Coordinate:     {}\n".format(self.coord)
        d += "          Town:     {}\n".format(self.town)
        d += "         River:     {}\n".format(self.river)
        d += " Typical Range:     {}\n".format(self.typical_range)
        return d
    
    # Function that checks whether a station is inconsistent
    
    def typical_range_consistent(self):
        
        a = self.typical_range
        
        if a == None:
            return False
        elif a[0] > a[1]:
            return False
        else:
            return True
    
    def relative_water_level(self):
        
        a = self.typical_range
        b = self.latest_level
        
        if self.typical_range_consistent and b != None and a != None:
            
            c = (b - a[0]) / (a[1] - a[0])
            c = round(c,2)
            return c
        

# Function that creates a list of inconsistent stations

def inconsistent_typical_range_stations(stations):
    
    inconsistent = []

    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == False:
            a = station.name
            inconsistent.append(a)
    
    return sorted(inconsistent)
        
            
        
        
        
        
        
