Information from REU 2018
Contact:
Name: Ryan Wong
Email: rwong5@u.rochester.edu
Github Link: 

To Initialize the Simulation Environment start with: sh clean.sh
    This will generate the necessary folders for data storage


The following files are included in this portion of the code:

Benchmark_Data
Contains all the benchmark files for 16 and 64 nodes. 
    Contains 3 types:
        1) Partitioned log files , those are the ones with #-#.txt or name#.txt
        2) Logfiles without memory txn. ie. NoMem_*.txt
        3) A combination of 1 & 2

ConfigGen.py 
    Generates N configurations via command: python ConfigGen.py N >> Name.txt

ConfigurationAnalysis
    Output directory for Simulation
DataConverter.py
    Converts output of simulator to input for Neural Network. 
    In here you may adjust the tuning parameters of how data is classified via:
        python DataConverter.py 
DataStorage
    Storage for data
LogCleanse.py
    Removes the memory transactions for any logfile via:
        python LogCleanse.py Filename >> Name.txt
OldFiles
    More storage, ConfigurationAnalysis/ and Output/ get moved here when clean
    script is ran 
Output
    Stores the detailed line by line simulation of the logfile
ParallelFiles
    Stores the configurations to be tested
Simulation2.py
    Simulator program
    python Simulation2.py {PathToBenchmarks} {PathToConfigurations}
    --Known issue, as of late the path to benchmark just cuts off the first 25
    chars of the path, I didn't have time to fix this, but it should split the
    path, take the last element and use that as a filename.
SimulationMaster.py
    Program to distribute instances of Simulation2 onto multiple nodes:
    mpirun -{MPI_ARGS} SimulationMaster.py PathToBenchmark PathToConfigurations
TF
    Provides Tensorflow programs.
    Neural net can be configured and ran in premade_estimator 
    config_data.py provides the path for input data how many classificaitons
    For additional information see TF.DNN.estimator
clean.sh
    Shell script to remove old data from previous simulation, this is
    automatically called when using SimulationMaster.py
config.py
    Provides tuning paramenters for hardware ie. volume factor, bandwidths, clk
    freq.
request.py
    Contains the class for each log line
