# file.py - Reads Road File(s) and Prints Results
#
# Author: Cameron Sims
# Date: 06/08/2024
#

# Required Imports #######################

# Internal Imports
import road     # Used to save data into

# External Imports
import csv      # Used to read a csv file

##########################################


# Read connection data from a file
def read_connection_manifest(filename, connections): 
    # Read the manifest file
    file = open(filename, "r")
    
    # Read the data
    data = csv.DictReader(file)
    
    # For all the lines in the file...
    for line in data:
        # Create a variable to use
        ID = int(line["id"])
        CRASH_INDEX = float(line["crash"])
        c = road.Connection(ID, CRASH_INDEX, [])
        
        connections.update({c.id: c})


# Read road data from a file
def read_road_manifest(filename, roads, connections):
    # Open the manifest file
    file = open(filename, "r")
    
    # Read the data
    data = csv.DictReader(file)
    
    # Get the Connection by ID
    def get_vertex(connections, id):
        return connections[id]
    
    # For all the lines in the file...
    for line in data:
        # Set which is used to find valeus with our ID
        ID = int(line["id"])
        NAME = line["name"]
        LENGTH = float(line["length"])
        SPEED = float(line["speed"])
        
        FROM = int(line["from"])
        TO = int(line["to"])
        
        # Connections
        CONS = [FROM, TO]
        
        # Vertexes
        FROM_V = get_vertex(connections, FROM)
        TO_V = get_vertex(connections, TO)
        # Add this road to both 
        FROM_V.connections.append(ID)
        TO_V.connections.append(ID)
        
        # Create a variable to use 
        r = road.Road(ID, NAME, LENGTH, SPEED, CONS)
        
        # Add this instance to the set
        roads.update({r.id: r})