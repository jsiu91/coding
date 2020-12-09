#!/usr/bin/env python3
### Star Triangle ###
import sys

def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1) +'*'*(2*x+1))

pyfunc(int(sys.argv[1]))
