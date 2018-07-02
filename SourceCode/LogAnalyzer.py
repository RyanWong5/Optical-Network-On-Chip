"""
Python file for analyzing logfiles and returning how much transmission goes
on between two nodes

"""
import os
import sys
from collections import OrderedDict
import operator




#Read Every Line in the logfile
#If we are analyizing a ring topology, convert from XY to ring 0-N
#Else add the line into the analyzer
def ReadLog(logfile, transactionList, topology):
   with open(logfile,'r') as logfile:
        for line in logfile:
            if(topology == 'ring'):
                tx = ConvertToRing(line)
                if(tx != None):
                    transactionList.append(ConvertToRing(line))
                else:
                    continue
            else:
                transactionList.append(line)
             


#For the ring configuration, maintain the same naming scheme as presented in 
#Simulator2.py 
#(1 0) = 0; (1 1) = 1; (1 2) = 2; (1 3) = 3; (1 4) = 4; 
#(1 5) = 5; (1 6) = 6; (1 7) = 7;
#(2 7) = 8; (2 6) = 9; (2 5) = 10; (2 4) = 11; (2 3) = 12;
#(2 2) = 13; (2 1) = 14; (2 0) = 15
#Any coordinate with a leading 0 is a tx to a memory module, which should be
#ignored for processor simulations

#Make a new log line formatted from XY coordinates to ring 0....N topology
#Format: Source, Destination, Packet Number, Packet Size, Time
def ConvertToRing(line):
#Split over spaces
    line = line.split()
#If the X coordinate is a 0, it means an access to memory which exists only in
#electrical domain - subject to change 
    if (int(line[0]) == 0 or int(line[2]) == 0):
        return None
    if (int(line[0]) == 1):
        source = int(line[1])
    else:
        source = int(8 * int(line[0]) - 1 - int(line[1]))
    if (int(line[2]) == 1):
        dest = int(line[3])
    else:
        dest = 8 * int(line[2]) - 1 - int(line[3])
    
    # To stay consistent with the simulator, we will always make 
    # node(source) < dest
    if source > dest:
        temp  = dest
        dest = source
        source = temp

    newLine = []
    newLine.append(str(source))
    newLine.append(str(dest))
    for oldLine in line[4:]:
        newLine.append(str(oldLine))
    #convert List to string
#    retLine = (' ').join(newLine)
    return newLine
    
#Define adjacent transactions as transactions that occur within 10 time of 
#each other
#For the first test we will not analyze the first transaction, only the 
#potentially overlapping transaction
def AdjacentTransactions(transactionList):
    #Define how close an 'adjacent transmission' is
    adjacencyTime = 4
    returnTransactions = []
    time = int(transactionList[0][-1])
    for transaction in transactionList[1:]:
        try:
            if(int(transaction[-1]) <= int(time) + adjacencyTime):
                returnTransactions.append(transaction)
            time = int(transaction[-1])
        except TypeError:
            print (transaction)

    return returnTransactions

        
def AnalyzeTraffic_Ring(transactions):
    connectivity = {}
    for tx in transactions:
        nodePair = (tx[0],tx[1]) 
        if nodePair in connectivity:
            txCount = connectivity.get(nodePair) 
            txCount = int(txCount) + 1
            connectivity[nodePair] = txCount
        else:
            connectivity[nodePair] = 1
    return connectivity

    
#Print the sorted values to a text file    
def DumpAnalysis(analyzedLog):
    with open('AnalyzedLog.txt' , 'a') as output:
        for pair,tx in sorted(analyzedLog.items(), key=lambda key: key[1]):
#            print (pair,tx)
            output.write(str(pair) + ' : ' +  str(tx) + '\n') 


def main():
    topology = str(sys.argv[2])
    logfile = str(sys.argv[1])
    #transactions = lines in a logfile
    transactions = []    
    ReadLog(logfile, transactions, topology)
#    for line in transactions:
#        print(line)
    
    #maybe we only look at transactions with time within 10 units of
    #each other? since non adjacent transactions will likely not have
    #overlapping requests
    overlapTransactions = AdjacentTransactions(transactions)

#    print(len(overlapTransactions))
    trafficLog = AnalyzeTraffic_Ring(overlapTransactions)
    DumpAnalysis(trafficLog)





if __name__ == '__main__':
    main()
