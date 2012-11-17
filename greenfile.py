
#!/usr/bin/python
import sys

if __name__ == "__main__":
    f = open(sys.argv[1])
    for line in f:
        print line.replace("\r\n", "")
    f.close()

