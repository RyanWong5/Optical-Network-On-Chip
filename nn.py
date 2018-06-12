# Generates a key array using nearest neighbour algorithm
# Only function to be called external is nearestNeighbourKeygen(),
# this functio is to be called with a proccessed benchmark logfile 
# as the sole argument.



import config
import time
import numpy as np

# borrowed code    
# def convXYtoNode(logFile):
#     benchmark = []

#     with open(logFile,"r") as bmread:
#         for line in bmread:
#             benchmarkLine = []
#             benchmarkItems = line.split()
#             for i in benchmarkItems:
#                 benchmarkLine.append(int(i))
#             benchmark.append(benchmarkLine)

#     newBenchmark = []
#     for row in benchmark:
#         if (row[0] != 0) & (row[2] != 0):
#             newRow = [(row[0] - 1) * 8 + row[1], (row[2] - 1) * 8 + row[3]]
#             newRow.extend(row[4:])
#             newBenchmark.append(newRow)
#     return newBenchmark
# def keyMapping(key):
#     for row in benchmark:
#         row[1] = key[row[1]]
#         row[2] = key[row[2]]

# startTime = time.time()
# nodeBenchmarkList = convXYtoNode(config.logFile)
# borrowed code

def rank():
    n = 0
    for row in trafficto:
        for i in range(0,n):
            if ~(row[4] == 0):
                trafpositions.append((n,i,row[i]))
        n += 1

def getsortkey(item):
    return item[2]


def NN(A, start):
    """Nearest neighbor algorithm.
    A is an NxN array indicating distance between N locations
    start is the index of the starting location
    Returns the path and cost of the found solution
    """
    path = [start]
    cost = 0
    N = A.shape[0]
    mask = np.ones(N, dtype=bool)  # boolean values indicating which 
                                   # locations have not been visited
    mask[start] = False

    for i in range(N-1):
        last = path[-1]
        next_ind = np.argmax(A[last][mask]) # find minimum of remaining locations
        next_loc = np.arange(N)[mask][next_ind] # convert to original location
        path.append(next_loc)
        mask[next_loc] = False

    return path

def nearestNeighbourKeygen(benchmark):

    trafficto = np.zeros((16,16))

    trafpositions = []

    for row in benchmark:
        print row[4]
        trafficto[row[0]][row[1]] += row[4]
        trafficto[row[1]][row[0]] += row[4]

    # for row in trafficto:
    # 	print row 

    #used to find highest trafic node pair to serve as a starting position
    rank()
    ntraffic = sorted(trafpositions, key=getsortkey)


    key = NN(trafficto, ntraffic[0][1])

    print "This is the neARST NEIGHBOUR key"
    print key
    return key


# print ntraffic

# for row in ntraffic:
#     s = row[1]
#     d = row[2]
#     #check key
#     if s in key:
#         if d in key:



