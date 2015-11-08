#!/usr/bin/env python

# hanoi.py
# Recursive and iterative solution to Towers of Hanoi

source = [10,9,8,6,5,4,3,2,1]
target = []
helper = []

def hanoi(num, source, helper, target):
   if num > 0:
       # Move n-1 to helper
       hanoi(num - 1, source, target, helper)

       # Move one disc from source to target
       if source:
           target.append(source.pop())

       # Move n - 1 from helper to target
       hanoi(num - 1, helper, source, target)

print source
hanoi(len(source), source, helper, target)
print target
