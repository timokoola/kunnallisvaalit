#!/usr/bin/python
import sys, md5

if __name__ == "__main__":
    f = open(sys.argv[1])
    dictset= set([])
    for line in f:
        res = [line[350:390].strip(), line[36:42], line[137:187].strip(),line[188:238].strip(), line[475:482]]
        key = res[0] + res[3] + res[2]
        if res[3].find("akkasvirta") != -1:
            print key,
        dictset.add(key.lower())
    f.close()
    dictset2 = set([])
    print "\n\n"

    f2 = open(sys.argv[2])
    for line in f2:
        res = line.split(";")
        key = res[0] + res[2] + res[3]
        if res[2].find("akkasvirta") != -1:
            print key,
        dictset2.add(key.lower())
    f2.close()
    print len(dictset), len(dictset2), len(dictset.intersection(dictset2))
    #print dictset ^ dictset2
