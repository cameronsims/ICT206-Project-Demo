# main.py - The main part of the program, everything links to here
#
# Author: Cameron Sims
# Date: 06/08/2024
#

# Required Imports ##########################

# Internal Imports
import display  # Used for printing and showing to user
import uinput   # Used for getting input from the user
import file     # Used for Reading Road Files
import graphing # Used for graphing
import road
import simulation # Used for running the simulation

# External Imports 
import random

#############################################

# We've loaded all our imports...

# These are the CSV files for the data we're reading (relative)
DATA_DIRECTORY = "./data"
ROAD_MANIFEST = DATA_DIRECTORY + "/roads.csv"             # Location of the road csv file
CONNECT_MANIFEST = DATA_DIRECTORY + "/connections.csv"    # Location of the connections csv file

# This where our file is going to be output (relative)
OUTPUT_DIRECTORY = "./out"
GRAPH_FILENAME = OUTPUT_DIRECTORY + "/graph.html"

# If all of our imports and variables worked...
# Then we will print out some things into the console

# Print Signature
display.print_signature()




# THIS IS WHERE THE PROGRAM BEGINS #

# Sets for quick access to road or connection data
# There cannot be a duplicate ID, which makes sense in-terms of our program
cons = {}    # Connection Map
roads = {}   # Road Map

# Read manifest(s)
display.print_connection_begin()

file.read_connection_manifest(CONNECT_MANIFEST, cons)
file.read_road_manifest      (ROAD_MANIFEST,    roads, cons)

display.print_connection_end()

# Get data for the simulation

# This is data for our driver, contains size and array of all drivers
# This is not a set as we are going to edit every single driver every single simulation cycle
# This will result in O(n), therefore we don't care if it is a set.
drivers_n   = uinput.get_driver_amount(display.print_error)
drivers = {}

# Re-generate driver
def driver_regenerate(driver):
    # This is the lowest ID of our roads.
    SMALLEST_ROAD_ID = min(roads)
    
    # This is the highest ID of our roads.
    BIGGEST_ROAD_ID = max(roads)
    
    # Floor and Cieling an ID
    FLOOR = SMALLEST_ROAD_ID #.id
    CIELING = BIGGEST_ROAD_ID #.id
    
    # Generate random numbers for our target destination and the beginning destination for the driver.
    currentID = random.randint(FLOOR, CIELING)
    targetID = random.randint(FLOOR, CIELING)
    
    # loop until we find a new one
    while currentID == targetID:
        targetID = random.randint(FLOOR, CIELING)
    
    # Target and Current
    driver.target = targetID
    driver.current = currentID
    
    # find new path
    driver.path = road.find_destination(roads, cons, currentID, targetID)




# Add the amount of drivers
for i in range(drivers_n):
    id = i + 1
    driver = road.Driver(-1 , -1)     # Create driver object
    driver_regenerate(driver)         # Generate a path...
    drivers.update({ id: driver })    # Append to array



# Get the amount of months we're running for (months * 30 * 24 = hours)
sim_months = uinput.get_sim_time(display.print_error)
sim_hours = sim_months * 30 * 24

# This is where the simulation begins
hours = sim_hours 

# This is data for the simulation
simulation_data = {
    "length": sim_hours*60,
    
    "intersections": {
        "length": len(cons)
    },
    
    "roads": {
        "length": len(roads)
    },

    "drivers": {
        "start": drivers_n,
        "deaths": 0,
        "end": -1
    }
}


# Run while we have hours to go...
while hours > 0:
    # Show how much hours there is left to go 
    display.print_hours(hours)
    
    # This is every minute for an hour...
    for minute in range(60):
        # Do some logic per tick... ##########################
        
        # Check drivers ######################################
        
        # Driver
        i = 0
        to_delete = []
        for id in drivers:
            # Get the driver object 
            driver = drivers[id]
            #print(driver.current, driver.target, driver.path, driver.progress)
            simulation.driver_update(driver, roads, cons, driver_regenerate)
            
            # Check if driver has died
            if driver.died:
                # Queue driver for deletion
                to_delete.append(id)
                simulation_data["drivers"]["deaths"] += 1
            
            i += 1
        
        # Remove the drivers from the array 
        for id in to_delete:
            drivers.pop(id)
        
        ######################################################=
    
    # Decrement the Hours
    hours = hours - 1

# Save data due to end of simulation 

simulation_data["drivers"]["end"] = len(drivers)

# End of simulation

# Display end of simulation...
print("Simulation Results:")
print("  Drivers:")
print("      Population (Start): ", simulation_data["drivers"]["start"])
print("      Population (End):   ", simulation_data["drivers"]["end"])
print("      Total Deaths:       ", simulation_data["drivers"]["deaths"])
print("  Roads:")
print("      Amount:             ", simulation_data["roads"]["length"])
print("  Intersections:")
print("      Amount:             ", simulation_data["intersections"]["length"])


# Create the graph
display.print_pyvis_begin()

graphing.create_graph(GRAPH_FILENAME, roads, cons)

display.print_pyvis_end()