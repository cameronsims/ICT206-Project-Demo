# road.py - Defines important classes to the system
#
# Author: Cameron Sims
# Date: 20/08/2024
#

import random   # used to calculate death percentage

# This is the update function it modifies how a driver runs, it runs every tick...
# - road: is the node that the node is across
# - regen_f: is a function that regenerates the path finding
def driver_update(driver, roads, connections, regen_f):
    # These are defines important for the function...
    
    road = roads[driver.current] # This is the road the driver is travelling across
   
    # If the driver has finished their trip across a road...
    if driver.progress >= 1.00:
        # Then pop the beginning of the queue and find the next connection to go down
        if len(driver.path) > 1:
            driver.path.pop(0)
            
            # Now find a new target...
            # Set the target to the next node.
            driver.current = driver.path[0]
            driver.progress = 0.00
            
            # Check the intersections crash rate...
            # First we have to find the intersection that we're heading towards
            for cid in road.connections:
                con = connections[cid]
                if driver.current in con.connections:
                    # Roll the dice to see death
                    dice = random.uniform(0.000000, 1.000000)
                    difference = abs(dice - con.crash)
                    # If the difference is too large, don't count it.
                    # But if the difference is small, kill the driver
                    if difference < 0.0001:
                        driver.died = True
                        # Log a new death that occured on the road.
                    break
        
        # If the driver is at their planned destination...
        if driver.target == driver.current:
            # Regenerate a driver
            regen_f(driver)
    # If the progress has no finished
    else:
        # Add to the progress...
        road_length = road.length
        road_speed = road.speed
        current_position = driver.progress * road_length
        current_progress = road_speed / 60
        driver.progress = driver.progress + current_progress
    # End of Driver - Update Function