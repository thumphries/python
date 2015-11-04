#!/usr/bin/env python

import os, re, sys
import string
from math import sqrt

# Here is a python comment


print "Hello, world!"

print (min(1, 2, 3, 4))

a = 4
item = 'teststring'
print('{a} {item}'.format(**locals()))

print ('item %d %s' % (a, item))

best = 'beststring'

hbar = '-' * 80
print hbar

abc = 'abc' * 24
print abc

print ('string is on the right'.rjust(80))

num = ord('A')

print (' '.join(map(str, [1, 2, 3])))

