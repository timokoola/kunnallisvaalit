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
        key = res[0].lower().strip() +" "+ res[2].lower().strip() +" "+ res[3].lower().strip()
        key = unicode(key.decode("ISO-8859-1", errors="strict"))
        values[key] = res
    f2.close()

    touched = set(values.keys())
    origlen = len(touched)

    tree = ET.parse(sys.argv[1])

    for elem in tree.iter(tag="candidate"):
        key = elem.attrib["home-municipality"].lower()
        key = key + " " + elem.attrib["last-name"].lower()
        key = key + " " + elem.attrib["first-name"].lower()
        print "checking " + key
        #valuekey = process.extractOne(key, values.keys()) 
        if values.has_key(key):
            if key in touched:
                touched.remove(key)
            print "matching at " + key 
            elem.attrib["values-liberal-conservative"] = values[key][4].strip().replace(",",".")
            elem.attrib["values-right-left"] = values[key][5].strip().replace(",",".")
            elem.attrib["values-green"] = values[key][6].strip().replace(",",".")
    tree.write("raaka-datat/edited_kv.xml")

    print touched

    print "unmatched %d/%d candidates" % (len(touched), origlen)

    #print dictset ^ dictset2
