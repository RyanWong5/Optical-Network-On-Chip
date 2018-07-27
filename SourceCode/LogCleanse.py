"""
python file for analyzing logfiles and returning how much transmission goes
on between two nodes

"""
import os
import sys




def classify(partitions, tx, grouping):
    line = tx.split(' ')
    time = line[-1]
    entry = (int(time) // grouping) 
    try:
        partitions[entry] = partitions[entry] + 1 
    except KeyError:
        entry = entry - 1
        print time
        partitions[entry] = partitions[entry] + 1

    


def CleanLog(logfile):
    name = logfile.split('/')
    path = name[:-1]
    path.append('/')
    path = ('/').join(path)
    name = name[-1]
    print(name)
    print(path)
    txn = []
#    minTime = +float('inf')
#    maxTime = -float('inf')
    minTime = sys.maxsize
    maxTime = -sys.maxsize - 1
    with open (logfile, 'r') as logfile:
        for line in logfile:
            time, line = ReadLines(line)  
            if time != None:
                time = int(time)
#                print time, line
            if line != None:
                txn.append(line)
                if time > maxTime:
                    maxTime = time
#                    print(maxTime)
                if time < minTime:
                    minTime = time
                    
        
    print('len of txn: ' , len(txn))
    
    #Define how many sub logs do you want
    numberOfPartitions = 5
    grouping = maxTime / numberOfPartitions
    partition ={}
    for i in range (0,5):
        partition[i] = 0
    
    print partition
    
    with open('NoMem-' + str(name),'a') as outfile:
        outfile.write(str(minTime) + ',' + str(maxTime) + '\n')
        for tx in txn:
            classify(partition,tx, grouping)
            outfile.write(tx + '\n')

    print partition
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
def ReadLines(line):
#Split over spaces
    line = line.split()
#If the X coordinate is a 0, it means an access to memory which exists only in
#electrical domain - subject to change 
    if (int(line[0]) == 0 or int(line[2]) == 0):
        return None,None
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
    newLine.extend(line[4:7])
#    print(newLine)
#    print(type(newLine))
    newLine = (' ').join(newLine)
#    print(newLine)
    if float(line[-1]) == 0:
        return 0,newLine
    else:
        return line[-1],newLine
    
        

def main():
    logfile = str(sys.argv[1])
    
    CleanLog(logfile)




if __name__ == '__main__':
    main()
