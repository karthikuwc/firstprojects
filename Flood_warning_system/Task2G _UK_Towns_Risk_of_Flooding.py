#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 16:12:17 2017

@author: Karthik Suresh

This program shows the UK towns and stations most at risk of flooding at any
given point in time. For the towns most at risk of flooding the program also
catagorizes the level of risk as low, moderate, high, severe. 

NB: Geopy python library needs to be installed for program to run. This can be 
done via terminal command 'pip install geopy'.
"""
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import avgradient
from floodsystem.utils import sorted_by_key
from floodsystem.geo import search_station

def run():
    
    # Build list of stations.
    stations = build_station_list()
    
    # Update each station with current water level.
    update_water_levels(stations)
    # Create list of all stations with critical nominal water level (not index).
    outp = stations_level_over_threshold(stations, 1.0)
    
    # Initialize dictionary to store (key(station): tuple(tuple(dates),
    # tuple(water level).
    stat_level = {}
    
    # Populate dictionary stat_level.
    for i in outp:
        # Find station in master list.
        station = search_station(stations, i[0])
            
        # Fetch data over past 2 days.
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id,
                                         dt=datetime.timedelta(days=dt))
        # Condition to only include stations for which 24 hour data could 
        # be recieved.
        if len(levels) > 96:
            stat_level[station.name] = (dates, levels)
    
    # Initialize dictionary to store key(station): value(gradient index).
    stat_poly = {}
    
    # Populate dictionary stat_level.
    for i in stat_level:
        
        stat_poly[i] = avgradient(stat_level[i][1])
        
    # Converting stat_poly dictionary to list of tuples that can be easily
    # printed and sorted.
    tupstat = []
    # Populating tupstat.
    for i in stat_poly:
        
        c = (i, stat_poly[i])
        tupstat.append(c)
    

    # Sorting stations in tupstat by water level index, highest first.    
    tupstat = sorted_by_key(tupstat, 1)
    tupstat.reverse()
    
    # Creates dictionary of towns of stations at risk and corresponding station
    # water level index.
    town_highlev = {}

    for i in tupstat:
        station = search_station(stations, i[0])
        
        if station.town != None:
            
            if station.town not in town_highlev:
                town_highlev[station.town] = [i[1]]
            else:
                town_highlev[station.town].append(i[1])
                
    # Converts dictionary to list of tuples.
    tuptown = []

    for i in town_highlev:
        c = (i, town_highlev[i])
        tuptown.append(c)
    
    # Sorting towns in tupstat by water level index, highest first.
    tuptown = sorted_by_key(tuptown, 1)
    tuptown.reverse()
    
    print("\n\n\n\nStations vs Flood Index\n\n")
    for i in tupstat:
        print("{}, {}\n".format(i[0], i[1]))
    
    print("\n\n\n\nTowns vs Flood Index\n\n")
    for i in tuptown:
        print("{}, {}\n".format(i[0], i[1]))
    
    # Assess risk level of flooding in each town by evaluating threat of
    # water level index. Create dictionary of risk level to towns.
    risk_level = {}
    risk_level["Severe"] = []
    risk_level["High"] = []
    risk_level["Moderate"] = []
    risk_level["Low"] = []
    
    # A water level index of 1.5 or higher is Severe, between 1.5 and 0.45 is
    # High, between 0.45 and 0 is Moderate, and below 0 is low.
    for i in tuptown:
        if i[1][0] > 1.5:
            risk_level["Severe"].append(i[0])
        elif i[1][0] > 0.45:
            risk_level["High"].append(i[0])
        elif i[1][0] > 0:
            risk_level["Moderate"].append(i[0])
        else:
            risk_level["Low"].append(i[0])
    
    if len(risk_level["Severe"]) != 0:
        severe = sorted(risk_level["Severe"])
    else:
        severe = "No Results"
    if len(risk_level["High"]) != 0:
        high = sorted(risk_level["High"])
    else:
        high = "No Results"
    if len(risk_level["Moderate"]) != 0:
        moderate = sorted(risk_level["Moderate"])
    else:
        moderate = "No Results"
    if len(risk_level["Low"]) != 0:
        low  = sorted(risk_level["Low"])
    else:
        low = "No Results"

    print("\n\n\n")
    print("Risk Level: Severe\n\n{}\n\n".format(severe))
    print("Risk Level: High\n\n{}\n\n".format(high))
    print("Risk Level: Moderate\n\n{}\n\n".format(moderate))
    print("Risk Level: Low\n\n{}\n\n".format(low))

# Execution of program.
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")

run()
