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
        if word.startswith("S"):
            print ('%s\t%s' % ("S", 1))
        elif word.startswith("R"):
            print ('%s\t%s' % ("R", 1))

        