"""
Python file for analyzing logfiles and returning how much transmission goes
on between two nodes

"""
import os
import sys





#Read Every Line in the logfile
#If we are analyizing a ring topology, convert from XY to ring 0-N
#Else add the line into the analyzer
def ReadLog(logfile, transactionList, topology):
   with open(logfile,'r') as logfile:
        for line in logfile:
            if(topology == 'ring'):
                transactionList.append(ConvertToRing(line))
            else:
                transactionList.append(line)
             


#For the ring configuration, maintain the same naming scheme as presented in 
#Simulator2.py 
#(1 0) = 0; (1 1) = 1; (1 2) = 2; (1 3) = 3; (1 4) = 4; 
#(1 5) = 5; (1 6) = 6; (1 7) = 7;
#(2 7) = 8; (2 6) = 9; (2 5) = 10; (2 4) = 11; (2 3) = 12;
#(2 2) = 13; (2 1) = 14; (2 0) = 15
#Well this is wrong....apparently? Wait on clarification from Prof. Z, 6/22

#Make a new log line formatted from XY coordinates to ring 0....N topology
#Format: Source, Destination, Packet Number, Packet Size, Time
def ConvertToRing(line):
#Split over spaces
    line = line.split()
    if (int(line[0]) == 1):
        source = int(line[1])
    else:
        source = int(8 * int(line[0]) - 1 - int(line[1]))
    if (int(line[2]) == 1):
        dest = int(line[3])
    else:
        dest = 8 * int(line[2]) - 1 - int(line[3])

    newLine = []
    newLine.append(str(source))
    newLine.append(str(dest))
    for oldLine in line[4:]:
        newLine.append(str(oldLine))
    #convert List to string
    retLine = (' ').join(newLine)
    return retLine
    
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
        if(int(transaction[-1]) <= int(time) + adjacencyTime):
            returnTransactions.append(transaction)
        time = transaction[-1]

    return returnTransactions

        


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
#    print len(overlapTransactions)
    print(overlapTransactions)







if __name__ == '__main__':
    main()
