#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:29:29 2017

@author: Karthik Suresh

This program plots the typical and current water levels of the 5 stations with
the highest current water level over the past ten days. 
"""

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

def run():

    # Build list of stations.
    stations = build_station_list()
    # Update the water level data for all stations in list of stations.
    update_water_levels(stations)
    # Creates a list of the 5 stations with the highest water levels.
    outp = stations_highest_rel_level(stations, 5)

    # For stations with highest water level, find 10 days historic water level
    # data.
    for i in outp:
        for station in stations:
            if station.name == i[0]:
                station_cam = station
                break
    
        # Fetch data over past 10 days
        dt = 10
        dates, levels = fetch_measure_levels(station_cam.measure_id,
                                             dt=datetime.timedelta(days=dt))
        
        # Plot typical levels and current water levels agaisnt time.
        plot_water_level_with_fit(station, dates, levels, 15)
    
    
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")

    run()