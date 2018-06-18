#!/usr/bin/python
"""
This master script is designed for use in the Salisbury University HPC lab
Probjected distribution nodes = 720
The goal is to distribute N independent simulations across all nodes.
Programmer: Ryan Wong
PI: Lei Zhang
python 2.7 compatible
"""

from mpi4py import MPI
import numpy as np
import sys 
import os
import subprocess


#Break the large Argument File into smaller files to be partitioned to the
#parallal version of the application
def partitionWork(inFile, nodes):
    configFile = inFile.split("-")
    configCount = configFile[1][:-4]
    print('Config Count: ', configCount, 'Node Count: ', nodes)
    #eachDivided file will get even number of nodes
    #if configurations/nodes != even number, distribute modulus of them
    eachWork = int(int(configCount) / nodes)
    totalRemainder = int(int(configCount) % nodes)
    print(eachWork, totalRemainder)
    distNode = 0
    internalWork = eachWork
    internalRemainder = totalRemainder
    extraLine = False
	#work assignment
    with open(inFile,"r") as masterConfig:
        for line in masterConfig:
            #No More extra work to be done - increment the node, reset the work
            with open ("ParallelFiles/ParallelConfigurations-" + \
                str(configCount) + "-" + str(distNode) + ".txt","a") \
                as distFile:
                distFile.write(line)
                print(distNode,line)
            internalWork -=1
#always decrement the work since a line has been done
#use extraLine as a flag to designate if an extraline has been added
#ie. taking away a value from the internal remainder
            if (internalWork <= 0 and internalRemainder != 0 and \
                extraLine == False):
                extraLine = True
                internalWork += 1
                internalRemainder -= 1
            if(internalWork <= 0 and extraLine == True):
                distNode += 1
                internalWork = eachWork
                extraLine = False
            elif(internalWork <= 0 and extraLine == False):
                distNode += 1
                internalWork = eachWork
#            print(distNode, internalWork,internalRemainder, extraLine)
    return configCount
    


def main():

    comm = MPI.COMM_WORLD
    nodeCount = comm.Get_size()
    rank = comm.Get_rank()
    #Get the current dir -> and the relative simulation configurations
    #Always Name Configuration folder as Configurations/
    path = os.getcwd()
    path = path + "/ParallelFiles/"
    #master thread/proc
    if(rank == 0):
    #prior to creating new files, delete old ones:
        clean = ['sh', 'clean.sh']
        subprocess.call(clean,shell=False)
    #If master, process the input file to be divided to nodes
        configCount = partitionWork(str(sys.argv[2]),nodeCount)    
    #distribute the work by sending which partition of the parallel file
        for i in range(1,nodeCount):
            #Which configuration file to process - configured to be: ParallelFiles/ParallelConfigurations-$(COUNT)-node.txt
            configName = "ParallelFiles/ParallelConfigurations-" + \
                str(configCount) + "-" + str(i) + ".txt" 
            print(configName)
            data = [str(sys.argv[1]), configName]
            req = comm.isend(data,dest = i , tag = i)

        #Do master thread's work
        pythonArg = ['python', 'Simulation2.py',str(sys.argv[1]), \
            str("ParallelFiles/ParallelConfigurations-" + \
            str(configCount) + "-0.txt"), str(rank)]
        print("being T" , rank)
        subprocess.call(pythonArg, shell=False)
    #slave threads
    elif(rank != 0):
        #Get data
        req = comm.irecv(source = 0, tag=rank)
        data =req.wait()
        logfile = data[0]
        configFile = data[1]
        #Form the argument list to to execute in the subprocess.
        #Set shell to false since using user defined arugments
        #rank arg passed for Identification
        pythonArg = ['python', 'Simulation2.py',str(logfile), str(configFile), str(rank)]
#        print("being T" , rank, logfile, configFile, rank)
        subprocess.call(pythonArg, shell=False)
        comm.Send('',dest = 0 , tag = nodeCount + rank)


    if (rank == 0):
        for nodeCollect in range (1,nodeCount):
            comm.Recv(data,source = nodeCollect, tag = nodeCount + rank)
        

         

if __name__ == '__main__':
    main()
