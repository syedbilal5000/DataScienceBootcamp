from ps3_partition import get_partitions
import time
import operator
filename="ps3_cow_data.txt"

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
    cow={}
    path='F:\\DSBootcamp\\Assignment 03\\'
    filename=path+filename
    file=open(filename,'r')
    data=file.read()
    split_data=data.split('\n')
    for row in split_data:
        row_split=row.split(',')
        name=row_split[0]
        weight=int(row_split[1])
        cow[name]=weight
    return cow

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
    cow = sorted(cows,key=cows.get,reverse=True)
    outerList = []
    while True:
        innerList = []
        total_value = 0
        for i in cow:
            if total_value + cows[i] <= limit:
                innerList.append(i)
                total_value += cows[i]
        outerList.append(innerList)
        tempList = []
        for i in cow:
            if i not in innerList:
               tempList.append(i) 
        cow = tempList
        if cow == []:
            break
    return outerList

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
    combinations = []
    for row in get_partitions(cows.keys()):
        combinations.append(row)
    
    outerList = []    
    for i in range(len(combinations)):
        innerList = []
        for j in range(len(combinations[i])):
            tempList = []
            for k in combinations[i][j]:
                tempList.append(cows[k])
            if sum(tempList) > limit:
                break
            innerList.append(combinations[i][j])
        if len(innerList) == len(combinations[i]):    
            outerList.append(innerList)
            
    num = []        
    for i in range(len(outerList)):
        num.append(len(outerList[i]))
              
    for i in outerList:
        if len(i) == min(num):
            return i
        
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
    cows=load_cows(filename)
    start=time.time()
    greedy=greedy_cow_transport(cows)
    end=time.time()
    timeGreedy=end-start
    tripGreedy=len(greedy)
    start=time.time()
    brute=brute_force_cow_transport(cows)
    end=time.time()
    timeBrute=end-start
    tripBrute=len(brute)
    print("          ----- Greedy -----")
    print("Number of trips: ",tripGreedy,", Time taken: ",timeGreedy)
    print("          ----- Brute -----")
    print("Number of trips: ",tripBrute,", Time taken: ",timeBrute)

compare_cow_transport_algorithms()

"""   ----- Write-up -----
1.    Greedy runs faster, because it took 0.0 time to execute
2.    Greedy does not return the optimal solution, because it will not check on possible combinations
3.    Brute does return the optimal solution, but it takes lot of memory and time.
"""