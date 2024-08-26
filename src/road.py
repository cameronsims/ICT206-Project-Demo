# road.py - Defines important classes to the system
#
# Author: Cameron Sims
# Date: 06/08/2024
#

#
# Connection Class
# - Defines a connection between at most 4 roads
#

class Connection:

    # The ID of the connection (-1 is an illegal ID)
    id = -1
    
    # What the connection connects to (MUST BE ROADS)
    connections = set()
    
    # This is the speed index (functions as the weight)
    # 0.01 - 100.00
    speed = 0.0
    
    # This is the crash index (how likely it is to crash in this intersection)
    # 0.0 - 100.0
    crash = 0.0
    
    # Constructor
    def __init__(self, id, crash, connections):
        # Set the ID
        self.id = id
        self.crash = crash
        
        self.connections = []
        
        # Add connections
        for link in connections:
            self.connections.append(link)
        
    # Equals
    def __eq__(self, other):
        return (self.id == other.id)
        
    # Lesser Than
    def __lt__(self, other):
        return (self.id < other.id)
   
    # Greater Than
    def __gt__(self, other):
        return (self.id > other.id)
        
    # Not Equal
    def __ne__(self, other):
        return not self.__eq__(other)
    
    # Lesser Than or Equal to
    def __le__(self, other):
        return not self.__gt__(self, other)
    
    # Greater Than or Equal To
    def __ge__(self, other):
        return not self.__lt__(self, other)
        
        
    # Hash Check, used in sets
    def __hash__(self):
        return int(self.id)


#
# Road class
# - Defines a way to get to place, needs to connect to a Connection
#

class Road:
    # The ID for the road
    id = -1
    
    # The name of the road
    name = "NULL"
    
    # The length of the class (u length)
    length = 0.0
    
    # The speed limit (u/hr)
    speed = 0.01
    
    # The Connections the road has to Connections
    connections = []
    
    # Constructor
    def __init__(self, id, name, length, speed, connections):
        # Set values
        self.id = id
        self.name = name
        self.length = length
        self.speed = speed

        self.connections = []
        
        # Add links to the array
        for link in connections:
            self.connections.append(link)
            
    # Equals
    def __eq__(self, other):
        return (self.id == other.id)
        
    # Lesser Than
    def __lt__(self, other):
        return (self.id < other.id)
   
    # Greater Than
    def __gt__(self, other):
        return (self.id > other.id)
        
    # Not Equal
    def __ne__(self, other):
        return not self.__eq__(other)
    
    # Lesser Than or Equal to
    def __le__(self, other):
        return not self.__gt__(self, other)
    
    # Greater Than or Equal To
    def __ge__(self, other):
        return not self.__lt__(self, other)
        
    
    # Hash Check, used in sets
    def __hash__(self):
        return int(self.id)

#
# Driver class
# - Defines a driver on the road
#
class Driver:
    # Target (Road)
    target = -1
    
    # Current (Connection)
    current = -1
    
    # The path of nodes
    path = []
    
    # This is a boolean which marks the driver for deletion
    died = False
    
    # Progress, this is a % of how much of the current node we've completed
    progress = 0.0
    
    # Initial
    def __init__(self, current, target):
        self.current = current
        self.target = target
        self.path = []

# This function gets the node relating to an id
def get_node(roads, goal):
    # This is a legacy function.
    return roads[goal]
    
# This function gets the node relating to an id
def get_vertex(connections, id):
    return connections[id]

# This is used recursively, to check nodes individually 
# - Returns true if not all have been visited...
# - False if all have been visited
def check_path(current, visited, destination):
    # Check all connections for our node.
    for c in current.connections:
        # Check visitation...
        if c not in visited or c == destination:
            return True
    # None were founds...
    return False
    

#
# find_destination(roads, location, destination)
# - This is a helper function to path find to a place.
#
def find_destination(roads, intersections, location, destination):
    # Check if location and destination are the same...
    if (location == destination):
        print(str(location) + " is the same node as " + str(destination))
        return []
    
    # This is where the current driver is.
    loc_node = -1
    
    # This is where the driver wants to go.
    dest_node = -1
    
    loc_node = roads[location]
    dest_node = roads[destination]
            
    # If either don't exist...
    #if not (loc_exists and dest_exists):
    #    print("No connection between " + str(location) + " and " + str(destination) + " exists")
    #    return []
        
    # Now try to find a connection between the two...
    # We're going to use a path finding algorithm of least resistance
    
    # This refers to the node iDs that have been visited
    visited = set()
    visited.add( location )
 
    # This function is to run recursively 
    def next_node(current, visited, destination):
        # This is the path that we find things using...
        path = [ current.id ]
        visited.add(current.id)
        
        # This MUST be a road... so check its speed 
        # If it isn't then this will crash our program to prevent non-roads 
        # from being parsed.
        current.speed
    
        # Check if this current node is the ID...
        if current.id == destination:
            # If it is, return the path
            #print("Found ID: " + str(destination))
            return path
        
        # Check our current node's avaliablity for searching...
        # If all the values have been searched...
        if not check_path(current, visited, destination):
            # Then return null, there is no way to get from one to the other...
            return [-1]
            
        # Otherwise, check the nodes that haven't been visited...
        for con in current.connections:
            # Get the actual connection 
            cnct = get_vertex(intersections, con)
            
            # Since current.connections is filled with Intersections (Connections)
            # we must check their roads...
            for r in cnct.connections:
                if r not in visited:
                    # If the result didn't come back with a result.
                    road = get_node(roads, r)
                    result = next_node(road, visited, destination)
                    
                    # If path is none...
                    
                    # If the result has a path...
                    #### print("RESULT: ", result)
                    if not result == [-1]:
                        # Then add the path to the visited and return
                        path = path + result
                        return path
        # If we somehow get here...
        # We did not find a connection in the path...
        # It cannot be in this connection, as we have tried every possible combination
        return [-1]
    
    # Loop while we haven't visited our destination node...
    max_iteration = len(roads)
    while (dest_node.id not in visited) and (max_iteration > 0):
        #### print("Trying to find a way to ", loc_node.id, dest_node.id)
        max_iteration -= 1
        return next_node(loc_node, visited, dest_node.id)