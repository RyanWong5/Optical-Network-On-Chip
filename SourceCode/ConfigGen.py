#!/usr/bin/python

import random as rand
import numpy as np
import sys

#Generate Random Configs

#18mins - 60k
#3hrs - 120k
#9hrs - 200k


def main():
    count = int(sys.argv[1])
#    print (count)
    configs=[]
    while(len(configs) < count): 
        config = ((rand.sample(range(0,16),16)))
#        print (config)
#if contains -> skip
        if any([x in config for x in configs]):
            continue
#else -> add a new config
        else:
            configs.append(config)
#            print len(configs)

        
#https://stackoverflow.com/questions/36117602/how-to-remove-the-square-brackets-from-a-list-when-it-is-printed-output
    for configuration in configs:
        print(",".join( repr(e) for e in configuration))




if __name__ == '__main__':
    main()
