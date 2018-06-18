"""
Python Script to convert the output given by the simulator to the input needed
by TensorFlow
Also Designed to fuse all data files into one
Convert from [config];time;rank -> node,node,node,node,rank
Programmer: Ryan Wong
PI: Lei Zhang
Note: This program will read any order of files, hence the ordering of the 
configurations will NOT be preserved
"""

import os
import fnmatch



#write a config line to file - removes spaces
def ParseLine(masterFile,line):
    line = line.split(', ')
    line = ','.join(line)
    masterFile.write(str(line)[1:-1])
   


#2.8856e-6 is the base ring in order 0-16 time 
#Change the classification levels here, also change the classifications
#Header file
def ClassifyByTime(time):
    time = float(time)
    if(time > 2.8856e-6):
        classification = '0'
    elif (time < 2.8856e-6):
        classification = '2'
    else:
        classification = '1'
#    print(time,classification)
    return classification

#The Header Line: #ofLinesToRead,nodeCount,Classifications,
def GenHeader(masterFile,count):
    masterFile.write(str(count) + ',16,')
    #Different Classifications can be added in here" - Naively we will use 
    #{Bad, Same, Good} - to specify relation to the in order ring config
    #Append new line at the end of header
    masterFile.write('Bad,Same,Good \r\n')


#This Function reads all the files in the list addFile, and fuseses the data 
#into a single csv
def ConvertFile(masterFile, addFile):
    #for every file in fileList, read it line by line and add them to the master
    for file in addFile:
        with open(file,'r') as read:
            for line in read:
                line = line.split(';')
                #write the config list- It is possible that the internal spaces
                ParseLine(masterFile,line[0])
                #Parse the time to see what level of classification it is
                classification = ClassifyByTime(line[1])
                masterFile.write(','+str(classification))
                #new line at the end of each entry
                masterFile.write('\r\n')
    

def main():
    #Keep a list of the output configurations that need to be fused
    files = []    

    #Filepath will either be specified via sys.argv or defaulted to the output
    #folder
    try:
        folder = str(sys.argv[1])
    except: 
        folder = 'ConfigurationAnalysis/'
    
    #for all the output files in the folder, add them to a list to be processed
    for file in os.listdir(folder):
        if fnmatch.fnmatch(file, 'ParallelConfigurations-*-*-Data*'):
            files.append(str(folder) + '/' + str(file))
        

    #If there are no generated datafiles from the simulation, or none were found
    #Exit the converter
    if(len(files)==0):
        print('No Configurational Data Files Found')
        exit()

    #get the number of configurations being fused
    configs =  files[0].split('-')
    numberOfConfigs = configs[1]
    
    
    #All TensorFlow data will be placed in TF folder
    outputDir = 'TF/'
    #Create the masterfile to append everything to
    masterFile = open(str(outputDir) + 'config-data-' + str(numberOfConfigs) \
         + '.csv', ('w+'))
    #Write the headerfile
    GenHeader(masterFile,numberOfConfigs)
    #Build the CSV
    ConvertFile(masterFile,files)
    
    
    
    
    


if __name__ == '__main__':
    main()
