"""
Python Script to convert the output given by the simulator to the input needed
by TensorFlow
Also Designed to fuse all data files into one
Convert from [config];time;rank -> node,node,node,node,rank
Programmer: Ryan Wong
PI: Lei Zhang
"""

def convertFile(file):





def main():
    #Keep a list of the output configurations that need to be fused
    files = []    

    #Filepath will either be specified via sys.argv or defaulted to the output
    #folder
    try:
        folder = sys.argv[1]
    except: 
        folder = ConfigurationAnalysis/
    
    #for all the output files in the folder, add them to a list to be processed
    for file in folder:
        files.append(file)
        



if __name__ == '__main__':
    main()
