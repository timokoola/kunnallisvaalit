#!/usr/bin/python
import sys

if __name__ == "__main__":
    f = open(sys.argv[1])
    arrs = set([])
    for line in f:
        if line.find("Vasemmisto") != -1:
            continue
        line = line.replace(",",".")
        line = line.replace("\r\n","")
        arr = line.split(";")
        x = int(float(arr[4])*4)
        y = int(float(arr[5])*4)
        z = float(arr[6]) 
        arrs.add(x)
        print "values[%d][%d] = %f;" % (x,y,z)
    f.close()

