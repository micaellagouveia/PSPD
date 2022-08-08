#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        if(len(word) == 6):
            print ('%s\t%s' % ("6", 1))
        elif(len(word) == 8):
            print('%s\t%s' % ("8", 1))
        elif(len(word) == 11):
            print('%s\t%s' % ("11", 1))
        