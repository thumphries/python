#!/usr/bin/env python

# 2Darray.py
# Basic 2D array usage

class Matrix:
    def __init__(self, rows, cols):
        self.array = [[0 for x in range(0, cols)] for x in range(0, rows)]
        self.rows = rows
        self.cols = cols

    def get(self, row, col):
        return self.array[row][col]

    def set(self, row, col, value):
        self.array[row][col] = value

    def to_string(self):
        # this is real dumb
        map(printit, self.array)

# Can't use print inside a lambda.
# print is a statement, not an expression (lol)
def printit(x):
    print x

grid = Matrix(10, 10)

grid.to_string()
print ""

x = 0
for i in range(10):
    for j in range(10):
        grid.set(i, j, x)
        x = x + 1

grid.to_string()
