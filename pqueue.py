#!/usr/bin/env python

# pqueue.py
# Basic usage of a priority queue

import Queue
import sys

nlines = int(sys.stdin.readline().rstrip())

# Read all ints from nlines of stdin and put them into the priority queue.
# Use the queue to sort, then print out in ascending order.

def asc():
    pq = Queue.PriorityQueue()

    for n in range(nlines):
        nums = map(int, sys.stdin.readline().rstrip().split())

        for x in nums:
            pq.put((x, str(x)))

    while not pq.empty():
       print pq.get()[1],
    print

# The simplest way to go in descending order seems to be to negate the priorities.
def desc():
    pq = Queue.PriorityQueue()

    for n in range(nlines):
        nums = map(int, sys.stdin.readline().rstrip().split())

        for x in nums:
            pq.put((-x, str(x)))

    while not pq.empty():
        print pq.get()[1],
    print

# asc()
# desc()
