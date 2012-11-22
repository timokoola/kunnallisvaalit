#!/usr/bin/python
import sys, md5
from fuzzywuzzy import process

if __name__ == "__main__":
    f = open(sys.argv[1])
    votes = {}
    for line in f:
        linearr = line.split(";")
        if int(linearr[01]) > 2:
            continue

        res = [line[350:390].strip(), line[36:42], line[137:187].strip(),line[188:238].strip(), line[475:482], int(line[453:460])]
        key = res[0] + " " + res[3]+ " " + res[2]
        val = votes.get(key.lower, 0) + res[5]
    f.close()

    f2 = open(sys.argv[2])
    values = {}
    for line in f2:
        res = line.split(";")
        key = res[0] +" "+ res[2] +" "+ res[3]
        values[key] = res
    f2.close()


    joined = {}
    for s in votes.keys():
        print ".",
        solve = process.extractOne(s,values.keys())
        if solve[1]  > 90:
            joined[s] = {"votes": votes[s], "values": values[solve[0]] } 
            print joined[s]



    #print dictset ^ dictset2
