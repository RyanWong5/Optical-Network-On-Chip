import config

class request:
    volumeTrack = 0
        
    # This is the initializer for the request class
    def __init__(self, theListOfInfo):
        self.sourceNode     = theListOfInfo[0] #Source node of request
        self.destNode       = theListOfInfo[1] #Destination node of request
        self.sequenceNumber = theListOfInfo[2] #Sequence number of request
        self.volume         = theListOfInfo[3] * \
            config.volume #Volume of request 
        self.volumeTrack    = theListOfInfo[3] * \
            config.volume #Volume of request
        volumeTrack         = theListOfInfo[3] * \
            config.volume #Volume of request
        self.Received       = theListOfInfo[4]
        self.timeStamp      = theListOfInfo[4] + config.EccToOcc + config.checkAvailability #Time of request
        self.timeTrack      = theListOfInfo[4] #Time of request
        self.scheduled      = False #If the request has already been through this process
        self.transmitted    = False #If the request has been transmitted
        self.right          = False #Track direction of path (-->)
        self.left           = False #Track direction of path (<--)
        self.waitTime       = 0 #Keeps track of how long the request has to wait
        self.distance       = [] #The distance between the soruce and dest nodes
        self.cost           = 0 #The cost of the data
        self.startTime      = 0 #When the data gets put in the network
        self.endTime        = 0 #When the data finishes transmitting
        self.nodestateNumber = 0 #Which network the data is running on
        self.tagged         = False #If the data has been put into the source or dest arrays (simulation2.py)
        self.positionSource       = 0 #The position of the source node of the data in the network
        self.positionDestination = 0 #The position of the destination node of the data in the network
        

    #Puts the requests in the network thereby taking up a path
    def schedule(self, nodestate, number):
        self.nodestateNumber = number
        
	#Makes source lower than destination for consistency
        if self.positionSource > self.positionDestination:
            temp = self.positionSource
            self.positionSource = self.positionDestination
            self.positionDestination = temp
            

	# Checks for shortest path
	# First if triggers if direct (e.g. 0 1 2 3...14a 15) path is the shortest or equadistant
        if (self.positionDestination - self.positionSource) <= (config.nodeCount - self.positionDestination + self.positionSource):
            
	    #Checks if that path is available (path is all 0s) and if so reserves path (makes it all 1s)
            if (nodestate[self.positionSource:(self.positionDestination + 1)] == [0] * (self.positionDestination + 1 - self.positionSource)):     
                nodestate[self.positionSource:(self.positionDestination + 1)] = [1] * ((self.positionDestination + 1) - self.positionSource)
                self.distance = [1] * ((self.positionDestination + 1) - self.positionSource)
                self.scheduled = True
                self.timeTrack += config.tBuffer + config.tMUX + config.tSequence + config.tSchedule # insert time parameters
                self.right = True

            #Checks if the other path is available (path is all 0s) and if so reserves path (makes it all 1s)
            elif ((nodestate[0:(self.positionSource + 1)] == [0] * (self.positionSource + 1))
            & (nodestate[self.positionDestination:] == [0] * (config.nodeCount - self.positionDestination))
            & (((self.positionSource + 1) + (config.nodeCount - self.positionDestination)) <= config.weighted_cutoff)):
    
                #Makes the left end of the path all 1s
                nodestate[0:(self.positionSource + 1)] = [1] * (self.positionSource + 1)
                #Makes the right end of the path all 1s
                nodestate[self.positionDestination:] = [1] * (config.nodeCount - self.positionDestination)

                self.distance = ([1] * (self.positionSource + 1)) + ([1] * (config.nodeCount - self.positionDestination))
                self.scheduled = True
                self.timeTrack += config.tBuffer + config.tMUX + config.tSequence + config.tSchedule# insert time parameters
                self.left = True
                
            #If path is not available add one to the time
            else:
                self.timeTrack += 1
                #self.waitTime += 1
                return False

        #Triggers if opposite direction path is shorter (e.g. 0 15 14 13...2 1)
        else:
            #Checks if that path is available (path is all 0s) and if so reserves path (makes it all 1s)
            if ((nodestate[0:(self.positionSource + 1)] == [0] * (self.positionSource + 1))
            & (nodestate[self.positionDestination:] == [0] * (config.nodeCount - self.positionDestination))):
                
                #Makes the left end of the path all 1s
                nodestate[0:(self.positionSource + 1)] = [1] * (self.positionSource + 1)
                #Makes the right end of the path all 1s
                nodestate[self.positionDestination:] = [1] * (config.nodeCount - self.positionDestination)

                self.distance = ([1] * (self.positionSource + 1)) + ([1] * (config.nodeCount - self.positionDestination))
                self.scheduled = True
                self.timeTrack += config.tBuffer + config.tMUX + config.tSequence + config.tSchedule# insert time parameters
                self.left = True

            #Checks if the other path is available (path is all 0s) and if so reserves path (makes it all 1s)
            elif ((nodestate[self.positionSource:(self.positionDestination + 1)] == [0] * (self.positionDestination + 1 - self.positionSource))
            & ((len(nodestate[self.positionSource:(self.positionDestination + 1)])) <= config.weighted_cutoff)):     
                nodestate[self.positionSource:(self.positionDestination + 1)] = [1] * ((self.positionDestination + 1) - self.positionSource)
                self.distance = [1] * ((self.positionDestination + 1) - self.positionSource)
                self.scheduled = True
                self.timeTrack += config.tBuffer + config.tMUX + config.tSequence + config.tSchedule # insert time parameters
                self.right = True
                    
            #If path is not available add one to the time since it cannot be processed yet
            else:
                self.timeTrack += 1
                #self.waitTime += 1
                return False

        #Transmission here
        if self.scheduled == True:
            volume = self.volume
            dataTransTime = volume*config.packetSize/(config.OCC*(10**9))
            self.timeTrack += config.tCloseChannels + config.tOpenChannels + dataTransTime #insert addition parameters
            self.transmitted = True
            return True

    #Deletes the request form the List of requests
    def delete_self(req):
        config.activeReq.remove(req)
        return

    #Releases the path the request took up (makes all the 1s into 0s)
    def release(self):
        #If the data is on the first network
        if (self.nodestateNumber == 1):
            # ------->
            if self.right == True:    
                config.nodestate1[self.positionSource:(self.positionDestination + 1)] = [0] * ((self.positionDestination + 1) - self.positionSource)
            # <-------
            elif self.left == True:
                #Makes the left end of the path all 0s
                config.nodestate1[0:(self.positionSource + 1)] = [0] * (self.positionSource + 1)
                #Makes the right end of the path all 0s
                config.nodestate1[self.positionDestination:] = [0] * (config.nodeCount - self.positionDestination)
            else:
                print "Shouldn't Print"
                config.nodestate1[self.positionSource:(self.positionDestination + 1)] = [0] * ((self.positionDestination + 1) - self.positionSource)
            self.delete_self() #Delete request
            
        #If the data is on the second network
        elif (self.nodestateNumber  == 2):
             # ------->
            if self.right == True:    
                config.nodestate2[self.positionSource:(self.positionDestination + 1)] = [0] * ((self.positionDestination + 1) - self.positionSource)
            # <-------
            elif self.left == True:
                #Makes the left end of the path all 0s
                config.nodestate2[0:(self.positionSource + 1)] = [0] * (self.positionSource + 1)
                #Makes the right end of the path all 0s
                config.nodestate2[self.positionDestination:] = [0] * (config.nodeCount - self.positionDestination)
            else:
                print "Shouldn't Print"
                config.nodestate2[self.positionSource:(self.positionDestination + 1)] = [0] * ((self.positionDestination + 1) - self.positionSource)
            self.delete_self() #Delete request

        #If the data is on the third network
        else:
            # ------->
            if self.right == True:    
                config.nodestate3[self.positionSource:(self.positionDestination + 1)] = [0] * ((self.positionDestination + 1) - self.positionSource)
            # <-------
            elif self.left == True:
                #Makes the left end of the path all 0s
                config.nodestate3[0:(self.positionSource + 1)] = [0] * (self.positionSource + 1)
                #Makes the right end of the path all 0s
                config.nodestate3[self.positionDestination:] = [0] * (config.nodeCount - self.positionDestination)
            else:
                print "Shouldn't Print"
                config.nodestate3[self.positionSource:(self.positionDestination + 1)] = [0] * ((self.positionDestination + 1) - self.positionSource)
            self.delete_self() #Delete request
        return
    

    #Sees if the request has already been scheduled or not
    def reqProcessing(self):
        self.release()
        return

    #Get the volume of the request
    def get_volumeTrack(self):
        return self.volumeTrack

    #Get the source node of the request
    def get_sourceNode(self):
        return self.sourceNode

    #Get the destination node of the request
    def get_destNode(self):
        return self.destNode
    
    #Get the sequence number of the request
    def get_sequenceNumber(self):
        return self.sequenceNumber

    #Get the wait time
    def get_waitTime(self):
        return self.waitTime

    def increment_waitTime(self):
        self.waitTime += 1

    #Sets the volume of the request
    def set_volumeTrack(self, number):
        #Subtracts the volume by the number given
        self.volumeTrack = self.volumeTrack - number
        return

    #Get the actual cost of this data
    def get_Cost(self):
        return self.cost

    #Set the cost of this data
    def set_Cost(self, numberTwo):
        self.cost = numberTwo
        return

    #Get when the data is put into the network
    def get_startTime(self):
        return self.startTime

    #Set when the data is put in the network
    def set_startTime(self, numberThree):
        self.startTime = numberThree
        return

    #Get when the data is finished transmitting (not including conversions(OccToEcc))
    def get_endTime(self):
        return self.endTime

    #Set when the data is done transmitting
    def set_endTime(self, numberFour):
        self.endTime = numberFour
        return

    #Set if the data has already been tagged (placed into the sourc and destination node arrays)
    def set_Tag(self, value):
        self.tagged = value
        return

    #Set the source position in the network where this data is
    def set_theSPosition(self, positionS):
        self.positionSource = positionS
        return

    #Set the destination node position in the network where this data is
    def set_theDPosition(self, positionD):
        self.positionDestination = positionD
        return

    #Get if this data has been tagged
    def get_Tag(self):
        return self.tagged

    #Get the current volume of this data
    def get_Volume(self):
        return self.volume

    #Get when this data is given to the simulator
    def get_timeStamp(self):
        return self.timeStamp

    #Get distance
    def get_Distance(self):
        return (len(self.distance) - 1)

    #Get direction that the request is traveling
    def get_Direction(self):
        if self.right == True:
            return "Right"
        elif self.left == True:
            return "Left"
        else:
            return "None"

    #Increase the wait time by 1
    def increase_waitTime(self):
        self.waitTime += 1

    def set_waitTime(self):
        self.waitTime = self.startTime - self.Received - config.EccToOcc - config.checkAvailability
        if self.waitTime < 0:
            self.waitTime = 0


    #Turns the object into a string
    def toString(self):
        return ('{:3} {:3} {:10} {:10} {:10} {:10} {:10} {:10} {:2}'.format(str(self.sourceNode), str(self.destNode), str(self.volume),
                str(self.Received), str(self.startTime), str(self.endTime), str(self.waitTime), str(self.cost), str(self.nodestateNumber)))

    def calcConnectivity(self):
        timeDelta = self.endTime - self.startTime
        volume = self.volume
        conn = (float)(volume/timeDelta)
        return (self.sourceNode, self.destNode, conn)
