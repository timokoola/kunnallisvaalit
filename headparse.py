#!/usr/bin/python
import sys, md5
from fuzzywuzzy import process

if __name__ == "__main__":
    f = open(sys.argv[1])
    dictset= set([])
    for line in f:
        linearr = line.split(";")
        if int(linearr[01]) > 2:
            continue

        res = [line[350:390].strip(), line[36:42], line[137:187].strip(),line[188:238].strip(), line[475:482]]
        key = res[0] + " " + res[3]+ " " + res[2]
        dictset.add(key.lower())
    f.close()
    dictset2 = set([])

    f2 = open(sys.argv[2])
    for line in f2:
        res = line.split(";")
        key = res[0] +" "+ res[2] +" "+ res[3]
        dictset2.add(key.lower())
    f2.close()

    print len(dictset),len (dictset2)

    for s in dictset:
        print ".",
        solve = process.extractOne(s,dictset2)
        if solve[1]  > 90:
            print s, solve



    #print dictset ^ dictset2
