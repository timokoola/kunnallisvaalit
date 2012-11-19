#!/usr/bin/python
import sys, md5

from fuzzywuzzy import process
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


if __name__ == "__main__":
    f2 = open(sys.argv[2])
    values = {}
    for line in f2:
        res = line.split(";")
        key = res[0] +" "+ res[2] +" "+ res[3]
        values[key] = res
    f2.close()

    tree = ET.parse(sys.argv[1])

    for elem in tree.iterfind("./election/electoral-area"):
        if elem.attrib["identifier"] == "01": # or  elem.attrib["identifier"] == "02":
            for item in elem.iterfind("./electoral-area/electoral-area/nominator/candidate"):
                key = item.attrib["home-municipality"].lower()
                key = key + " " + item.attrib["last-name"].lower()
                key = key + " " + item.attrib["first-name"].lower()
                print "checking " + key
                valuekey =  process.extractOne(key, values.keys())
                if valuekey[1]  > 90:
                    print "matching at " + key 
                    elem.attrib["values-liberal-conservative"] = values[valuekey[0]][4]
                    elem.attrib["values-right-left"] = values[valuekey[0]][5]
                    elem.attrib["values-green"] = values[valuekey[0]][6]
            pass
        else:
            del[elem]

    tree.write("raaka-datat/adited_kv.xml")





    #print dictset ^ dictset2
