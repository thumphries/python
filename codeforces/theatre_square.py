#!/usr/env/bin/python
# -*- coding: utf-8 -*-

# theatre_square.py
#
# A. Theatre Square
# time limit per test2 seconds
# memory limit per test64 megabytes
# inputstandard input
# outputstandard output
#
# Theatre Square in the capital city of Berland has a rectangular
# shape with the size n * m meters. On the occasion of the city's
# anniversary, a decision was taken to pave the Square with square
# granite flagstones. Each flagstone is of the size a * a.
#
# What is the least number of flagstones needed to pave the Square?
# It's allowed to cover the surface larger than the Theatre Square,
# but the Square has to be covered. It's not allowed to break the
# flagstones. The sides of flagstones should be parallel to the sides
# of the Square.
#
# Input The input contains three positive integer numbers in the first
# line: n,  m and a (1 <=  n, m, a <= 10^9).
#
# Output
# Write the needed number of flagstones.
#
# Sample test(s)
# input
# 6 6 4
# output
# 4

import sys

def divround(a,b):
    return (a + (b - 1)) / b

input = map(int, sys.stdin.readline().rstrip().split())

a = input.pop()
m = input.pop()
n = input.pop()

result = divround(n, a) * divround(m, a)

print result
