###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cow_dict = {}
    
    file = open(filename)
    
    for line in file:
        current_line = line.split(",") #separate lines to list of names/weights
        current_line[1] = current_line[1].strip() #cut off \n from weight

        cow_dict[current_line[0]] = int(current_line[1]) #store variables to dictionary
    file.close()

    return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    #create new dictionary and sort cow dictionary from heaviest to lightest weight
    cows_sort = {}
    for cow in sorted(cows, key = cows.get, reverse = True):
        cows_sort[cow] = cows[cow]
    

    trips = []
    cows_taken = []
    
    #loop until every cow is selected
    while len(cows_sort) > len(cows_taken): 
        #zero out trip cows and weight
        current_trip = [] 
        weight = 0
        
        #go through sorted list of cows
        for current_cow in cows_sort:
            #add cow to current trip if it doesn't exceed weight and it hasn't already been selected
            if (weight + cows_sort[current_cow] <= limit) and current_cow not in cows_taken:
                current_trip.append(current_cow)
                weight += cows_sort[current_cow]
                cows_taken.append(current_cow)
        
        #add current trip to trips once it reaches the weight limit and cycled through all the remaining cows        
        trips.append(current_trip)

    return trips
        
    #choose heaviest cow and add it to list while current list is under weight
    #return list

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips 
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #set initial best of 10 cows on separate trips
    best = list(cows.keys())

    #go through each unique partition of set of cows
    for part in get_partitions(cows):
        #use valid_weight to track if a trip exceeds 10 tonnes
        valid_weight = True
        
        #go through each grouping of cows in the partition
        for trip in part:
            #set trip weight equal to zero at the start of each trip
            trip_weight = 0 
            for cow in trip:
                #sum up cow weight for the trip
                trip_weight += cows[cow]
            #if the trip weight exceeds the limit, that part isn't valid
            if trip_weight > limit:
                valid_weight = False
        #if current partition has fewer trips than previous best, mark it
        if valid_weight and len(part) < len(best):
            best = part
    
    return best
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows('ps1_cow_data.txt')
    start = time.time()
    greedy_cow_transport(cows)
    end = time.time()
    
    greedy_time = end - start
    
    start = time.time()
    brute_force_cow_transport(cows)
    end = time.time()
    
    brute_time = end - start
    
    return ['greedy time:',greedy_time, 'brute time:', brute_time]
    
