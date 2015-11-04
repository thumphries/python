#!/usr/bin/env python

# tree.py
# very basic tree with traversals

import sys

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, node):
        if (self.root == None):
            self.root = node
        else:
            self.root.insert(node)

    def list(self):
        result = []
        if (self.root):
            self.root.inorder(result.append)
        return result

    def list_nonrec(self):
        result = []
        if (self.root):
            self.root.inorder_nonrec(result.append)
        return result

class Node(object):
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self, node):
        if (node.value > self.value):
            self.insert_right(node)
        elif (node.value < self.value):
            self.insert_left(node)
        else:
            return

    def insert_right(self, node):
        if (self.right == None):
            self.right = node
        else:
            self.right.insert(node)

    def insert_left(self, node):
        if (self.left == None):
            self.left = node
        else:
            self.left.insert(node)

    def inorder(self, fun):
        if (self.left):
            self.left.inorder(fun)
        fun(self.value)
        if (self.right):
            self.right.inorder(fun)

    def preorder(self, fun):
        fun(self.value)
        if (self.left):
            self.left.preorder(fun)
        if (self.right):
            self.right.preorder(fun)

    def inorder_nonrec(self, fun):
        stack = [self]
        visited = {}

        while (stack):
            t = stack.pop()
            if (t not in visited):
                if (t.right):
                    stack.append(t.right)
                visited[t] = 1
                stack.append(t)
                if (t.left):
                    stack.append(t.left)
            else:
                fun(t.value)

tree = Tree()
tree.insert(Node(5))
tree.insert(Node(1))
tree.insert(Node(9))
tree.insert(Node(100))
tree.insert(Node(150))

print(tree.list_nonrec())
