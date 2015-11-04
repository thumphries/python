#!/usr/bin/env python

# digits.py
# Input: A stream of text
# Output: The same stream, with:
#             - every digit less than 5 replaced with <
#             - every digit greater than 5 replaced with >
#
# eg: 123456789abcde -> <<<<5>>>>abcde

import re, sys

def main():
    less = re.compile('[01234]')
    more = re.compile('[6789]')

    for line in sys.stdin:
        input1 = less.sub('<', line)
        output = more.sub('>', input1)
        sys.stdout.write(output)

main()
