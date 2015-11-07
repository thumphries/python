#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Find the first zero in a byte
# There's a hardware instruction for this that you'd need cython for probably
def find_first_zero(ord):
    pos = 0
    mask = 0b10000000

    # print ("%s" % (bin(mask)))
    # print ("%s" % (bin((mask >> 1) | 0b10000000)))
    # print ("%.10s & %.10s = %.10s" % (bin(ord), bin(mask), bin(ord & mask)))

    while ord & mask and pos < 8:
        # print ("%s & %s = %s" % (bin(ord), bin(mask), bin(ord & mask)))
        mask = mask >> 1
        pos = pos + 1

    return (pos if pos < 8 else -1)

# print (find_first_zero(0b00000000))
# print (find_first_zero(0b01111111))
# print (find_first_zero(0b11011111))
# print (find_first_zero(0b11111100))

# return an integer utf8 codepoint from the string
# else raise UnicodeDecodeError
def decode_codepoint(string):
    if not len(string):
        raise

    # First zero indicates the run length
    pos = find_first_zero(string[0])

    if pos < 0 or pos == 1 or pos == 7:
        # Invalid first byte
        raise

    # Check length
    if pos == 0 and len(string) > 0:
        raise Exception("Too long!")

    if pos > 1 and len(string) != pos:
        raise Exception("Wrong length!")

    # Get the remnants of the first byte
    firstmask = (2 ** pos) - 1
    res = string.pop(0) & firstmask
    test = 0b11000000
    mask = 0b00111111

    for b in string:
        if b & test != 0b10000000:
            raise
        else:
            res = (res << 6) | (b & mask)

    return res

print ("U+%.4x = U+00a2?" %
  ((decode_codepoint([0b11000010, 0b10100010]))))
print ("U+%.4x = U+20ac?" %
  (decode_codepoint([0b11100010, 0b10000010, 0b10101100])))
print ("U+%.4x = U+10348?" %
  (decode_codepoint([0b11110000, 0b10010000, 0b10001101, 0b10001000])))

try:
    print ("U+%.4x != U+10348?" %
        (decode_codepoint([0b11110000, 0b10010000])))
    print "Too short: failed"
except:
    print "Too short: passed"
finally:
    pass

try:
    print ("U+%.4x = U+10348?" %
        (decode_codepoint([0b11110000, 0b10010000, 0b10001101, 0b10001000, 0b10001000])))
    print "Too long: failed"
except:
    print "Too long: passed"
finally:
    pass

try:
    print ("U+%.4x = U+10348?" %
        (decode_codepoint([0b11110000, 0b11010000, 0b10001101, 0b10001000])))
    print "Bad byte: failed"
except:
    print "Bad byte: passed"
finally:
    pass
