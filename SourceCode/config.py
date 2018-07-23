import os, sys


# Pre: Requires correct directory of benchmarks in variable path
# Post: Creates list of benchmarks
#path = 'C:/Users/nxconrad/Desktop/REU 2.0/Benchmark Data/16-core/7'
#edit to path to get it based on current local dir
path = os.getcwd()
path = path + '/Benchmark_Data/16-core/7'
#print(path)
dirs = os.listdir(path)
#print (dirs)
benchmarks = []
benchmarksOnly = []

# Appends all benchmarks in directory into one list

for file in dirs:
    benchmarks.append(file)
    benchmarksOnly.append(file)
for i in range(0,len(benchmarks)):
    benchmarks[i] = path + '/' + benchmarks[i]
nodeCount = 16
activeReq = [] #The list of requests received
nodestate1 = [0]*nodeCount #first frequency loop
nodestate2 = [0]*nodeCount #second frequency loop   
nodestate3 = [0]*nodeCount #third frequency loop
frequencies = 1 #Changes the number of loops that can be used to process requests (Change at will)
OCC = 40 #GHz (Change at will)
ECC = 2 #GHz (Change at will)
packetSize = 8*(10**9) #bits
volume = 10  #Volume Factor, Change this at will as well

##EDIT HERE FOR CONFIGURATIONS -- this should eventually be made into arguments -RW
#print ("Enter log file")
#print ("Len: ",len(sys.argv))
#if given sys args use sys args over default -RW
if (len(sys.argv) >= 3):
    logFile=sys.argv[1][25:]
#    logFile=logFile.split('/')
#    logFile=logFile[-1]
    configurationFile=sys.argv[2]
	#configurationFilePath=sys.argv[2]
	#configruationSplit = configurationFilePath.split("/")
	#configurationFile = configruationSplit[-1]
#    print("the config file: ", configurationFile)
else:
	logFile = 'flow_freqmine100#2.txt'#'flow_dedup.log'#'test_walston_004.log' the log file that will be tested
	configurationFile = 'AllConfigurations-5.txt' #The file with only configurations in it.
weighted_cutoff = 20 # max nodes allowed to be bypassed on furthest path (Change at will)


#Global time constants to account for certain processes.
checkAvailability = 1 #Constant to check if the channels are available (Change at will)
EccToOcc       = 1 #Constant to turn the electrical signal into an optical one (Change at will)
OccToEcc       = 5 #Constant to turn the optical signal into an electrical one (Change at will)
tBuffer        = 1 *EccToOcc
tMUX           = 1 *EccToOcc
tSequence      = 1 *EccToOcc
tSchedule      = 1 *EccToOcc
tInitialize = tBuffer + tMUX + tSequence + tSchedule
tOpenChannels  = 1 *EccToOcc
tCloseChannels = 1 *EccToOcc

tInitialize = tBuffer + tMUX + tSequence + tSchedule
tChannelAloc = tOpenChannels + tCloseChannels

#Global clock cycle constant for tracking t clock intervals
t = 0
