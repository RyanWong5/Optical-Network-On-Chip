#  File name: 	benchmarkread.py
#  Description: Reads in a log file from a benchmark. Assumes the log is for 16 cores 
#				and that source and destination nodes are in 2-d coordinates Creates 
#				an out list with 2-d source and destination coordinates mapped to 
#				1-d. Assumes that any x coordinate 
# 				that is zero is to memory and is ignored. 
#				Mapping is as follows 
#				(x is along the hoziontal and y is along the verticle):
# 				 |0 1  2  3  4  5  6  7
# 				-|---------------------
# 				1|0 1  2  3  4  5  6  7
# 				2|8 9 10 11 12 13 14 15
#
# Author:		B. Davison 6-21-16

#!/usr/bin/python	

filename = "flow_barnes.log"
benchmark = []

with open(filename,"r") as bmread:
	for line in bmread:
		b = []
		q = line.split()
		for i in q:
			b.append(int(i))
		benchmark.append(b)

out = []
## this is the original
##for row in benchmark:
##	if (row[0] != 0) & (row[2] != 0):
##                d = [(row[0] - 1) * 8 + row[1], (row[2] - 1) * 8 + row[3]]
##                d.extend(row[4:])
##                out.append(d)

##this is attempt to fix               
##for row in benchmark:
##	if (row[0] != 0) & (row[2] != 0):
##                if (row[0] = 1) & (row[2] = 1):
##                        d = [(row[0] - 1) * 8 + row[1], (row[2] - 1) * 8 + row[3]]
##                        d.extend(row[4:])
##                        out.append(d)
##                if (row[0] = 2) & (row[2] = 2):
##                        d = [(row[0] - 1) * 8 + (7 - row[1]), (row[2] - 1) * 8 + (7 - row[3])]
##                        d.extend(row[4:])
##                        out.append(d)
##                if (row[0] = 1) & (row[2] = 2):
##                        d = [(row[0] - 1) * 8 + row[1], (row[2] - 1) * 8 + (7 - row[3])]
##                        d.extend(row[4:])
##                        out.append(d)
##                if (row[0] = 2) & (row[2] = 1):
##                        d = [(row[0] - 1) * 8 + (7 - row[1]), (row[2] - 1) * 8 + row[3]]
##                        d.extend(row[4:])
##                        out.append(d)                        
##                        
                        
        





