#!/usr/bin/env python
# -*- coding: utf-8 -*-

# B. Taxi
# time limit per test3 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
#
# After the lessons n groups of schoolchildren went outside and
# decided to visit Polycarpus to celebrate his birthday. We know that
# the i-th group consists of si friends (1 ≤ si ≤ 4), and they want to
# go to Polycarpus together. They decided to get there by taxi. Each
# car can carry at most four passengers. What minimum number of cars
# will the children need if all members of each group should ride in
# the same taxi (but one taxi can take more than one group)?
#  
# Input
#
# The first line contains integer n (1 ≤ n ≤ 105) — the number of
# groups of schoolchildren. The second line contains a sequence of
# integers s1, s2, ..., sn (1 ≤ si ≤ 4). The integers are separated by
# a space, si is the number of children in the i-th group.
#  
# Output
#
# Print the single number — the minimum number of taxis necessary to
# drive all children to Polycarpus.
#  
# Sample test(s)
# input
# 5
# 1 2 4 3 3
# output
# 4
# input
# 8
# 2 3 4 4 2 1 3 1
# output
# 5
# Note
# In the first test we can sort the children into four cars like this:
#  
# the third group (consisting of four children),
# the fourth group (consisting of three children),
# the fifth group (consisting of three children),
# the first and the second group (consisting of one and two children, correspondingly).
# There are other ways to sort the groups into four cars.

import sys

ngroups = int(sys.stdin.readline().rstrip())
groups = map(int, sys.stdin.readline().rstrip().split())

groupings = { '1': 0, '2': 0, '3': 0, '4': 0 }

for x in range(ngroups):
    key = str(groups[x])
    groupings[key] = groupings[key] + 1

taxis = groupings['4'] + groupings['3']

# Every group of one can ride with a group of 3
if (groupings['3'] > 0 and groupings['1'] > 0):
    groupings['1'] = groupings['1'] - min(groupings['1'], groupings['3'])

# Can combine every four groups of one
# i.e. taxis += ones / 4
#      taxis += twos / 2
#      all the modulos get their own

taxis = taxis + (groupings['2'] / 2)
groupings['2'] = groupings['2'] - (2 * (groupings['2']/2))
taxis = taxis + (groupings['1'] / 4)
groupings['1'] = groupings['1'] - (4 * (groupings['1'] / 4))

# Could still have 1 group of 2 and up to 3 groups of 1
if (groupings['2']):
    taxis = taxis + 1

if (groupings['1'] > 2 and groupings['2']):
    taxis = taxis + 1
elif (groupings['1'] and not groupings['2']):
    taxis = taxis + 1

print taxis