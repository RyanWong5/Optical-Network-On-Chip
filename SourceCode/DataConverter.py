"""
Python Script to convert the output given by the simulator to the input needed
by TensorFlow
Also Designed to fuse all data files into one
Convert from [config];time;rank -> node,node,node,node,rank
Programmer: Ryan Wong
PI: Lei Zhang
"""

import os
import fnmatch


#The Header Line: #ofLinesToRead,nodeCount,Classifications,
def GenHeader(masterFile,count):
    masterFile.write(str(count) + ',16,')
    #Different Classifications can be added in here" - Naively we will use 
    #{Bad, Same, Good} - to specify relation to the in order ring config
    masterFile.write('Bad,Same,Good')


#This Function reads all the files in the list addFile, and fuseses the data 
#into a single csv
def ConvertFile(masterFile, addFile):
    #for every file in fileList, read it line by line and add them to the master
    for file in addFile:
       """TODO""" 

def main():
    #Keep a list of the output configurations that need to be fused
    files = []    

    #Filepath will either be specified via sys.argv or defaulted to the output
    #folder
    try:
        folder = str(sys.argv[1])
    except: 
        folder = "ConfigurationAnalysis/"
    
    #for all the output files in the folder, add them to a list to be processed
    for file in os.listdir(folder):
        if fnmatch.fnmatch(file, 'ParallelConfigurations-*-*-Data*'):
            files.append(file)
        

    #get the number of configurations being fused
    configs =  files[0].split('-')
    numberOfConfigs = configs[1]
    
    
    #Create the masterfile to append everything to
    masterFile = open("config-data-" + str(numberOfConfigs) + ".csv", ("w+"))
    #Write the headerfile
    GenHeader(masterFile,numberOfConfigs)
    #Build the CSV
    ConvertFile(masterFile,files)
    
    
    
    
    


if __name__ == '__main__':
    main()
