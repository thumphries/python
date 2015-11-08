#!/usr/bin/env python

# anagram.py
# Print if two words are anagrams of each other in various ways
# Constrained to ASCII upper and lower case

import sys, string

def main():
    nlines = int(sys.stdin.readline().rstrip())

    for x in range(nlines):
        words = sys.stdin.readline().rstrip().split()
        if anagram_dict(words[0], words[1]):
            print ("%s is an anagram of %s" % (words[0], words[1]))

# Lazy but complex (O(n log n), where n is the longer of the two strings)
def anagram_sort(s1, s2):
    return ''.join(sorted(s1)) == ''.join(sorted(s2))

# Constant space and linear time, [a-zA-Z] only
def anagram_array(s1, s2):
    histo1 = [0 for x in range(26)]
    histo2 = [0 for x in range(26)]
    s1_lower = s1.lower()
    s2_lower = s2.lower()

    for x in s1_lower:
        idx = ord(x) - ord('a')
        if idx >= 26 or idx < 0:
            return False
        histo1[idx] = histo1[idx] + 1

    for x in s2_lower:
        idx = ord(x) - ord('a')
        if idx >= 26 or idx < 0:
            return False
        histo2[idx] = histo2[idx] + 1

    return histo1 == histo2

# Space: linear in the number of unique letters
# Time: linear in the larger of string length OR number of unique letters
# This one handles unicode, nice!
def anagram_dict(s1, s2):
    histo1 = {}
    histo2 = {}
    s1_lower = s1.lower()
    s2_lower = s2.lower()

    for x in s1_lower:
        histo1[x] = histo1.get(x, 0) + 1

    for x in s2_lower:
        histo2[x] = histo2.get(x, 0) + 1

    return histo1 == histo2


main()
