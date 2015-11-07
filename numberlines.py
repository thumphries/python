#!/usr/bin/env python

# numberlines.py
# Basic thing for parsing lines of numbers, ACM-style.
# - First line of input is the number of lines to follow
# - Each line has an arbitrary number of integers
# - For each line, print the number of terms, and their sum.
#
# ACM-style means 'do not bother with invalid input'
#
# e.g.
# in:
# 2
# 1 2 3 4 5
# 6 7 8 9 10
#
# out:
# 5 15
# 5 40

import sys

count = sys.stdin.readline()
num_lines = int(count.rstrip())

for i in range(0, num_lines):
    sum = 0
    count = 0
    line = sys.stdin.readline().rstrip().split()
    for word in line:
        count = count + 1
        sum += int(word)
    print ("%d %d" % (count, sum))

