#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

class Tree():
    def __init__(self, data, left=None, right=None):
        self.data   = data
        self.left   = left
        self.right  = right

    def __str__(self):
        return str(self.data) + "\n\t" + str(self.left.data) + "\n\t" + str(self.right.data)

    def traverse(self):
        thislevel = [self]
        while thislevel:
            nextlevel = list()
            firstOfLevel = True
            for n in thislevel:
                print n.data,
                if (firstOfLevel):
                    firstOfLevel=False
                    if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            print
            thislevel = nextlevel

# Read the file containing the triangle and 
# store it as a binary tree
def readFile():
    # Get lines of the file
    with open('./triangle', 'r') as f:
        lines = f.readlines()

    # Create root node
    d = int(lines[0].replace("\n", ''))
    root = Tree(d)

    currentNodes = [root]

    # Get each node its two children
    for line in lines[1:]:
        nextNodes = []

        # Create nodes based on the next line
        for d in line.replace("\n" , '').split(' '):
            nextNodes.append(Tree(d))

        # Append the new nodes as children
        for n in xrange(len(currentNodes)):
            currentNodes[n].left = nextNodes[n]
            currentNodes[n].right = nextNodes[n+1]

        currentNodes = nextNodes

    return root

# Dumb algorithm: from the root take the bigger child
def followBestPath(root):
    path = [root.data]

    while (not (root.left is None and root.right is None)):

        if (root.left is None):
            leftStr = "None"
        else:
            leftStr = str(root.left.data)
        if (root.right is None):
            rightStr = "None"
        else:
            rightStr = str(root.right.data)
        string =  "Root : " + str(root.data) + "\tl " + leftStr + "\tr " + rightStr

        if ((not root.left is None) and (root.left.data > root.right.data)):
            path.append(int(root.left.data))
            root = root.left
        else:
            path.append(int(root.right.data))
            root = root.right

    return path

def readFile2():
    # Get lines of the file
    with open('./triangle', 'r') as f:
        fileLines = f.readlines()

    # Transform the lines as lists of int
    lines = []
    for line in fileLines:
        lines.append([ int(i) for i in line.replace("\n", '').split(' ')])

    # Find maximum path
    for i in reversed(xrange(len(lines)-1)):
        newLine = []
        for j in xrange(len(lines[i])):
            if (lines[i+1][j] > lines[i+1][j+1]):
                newLine.append(lines[i][j] + lines[i+1][j])
            else:
                newLine.append(lines[i][j] + lines[i+1][j+1])
        lines[i] = newLine


    for l in lines:
        print l

    # Maximum path:
    print "maximum path: " + str(lines[0][0])


def main():
    readFile2()

main()
