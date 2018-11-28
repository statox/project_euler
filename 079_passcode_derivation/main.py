#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Remember to use the virtualenv to get networkx to create a graph

import networkx as nx


def main():
    with open('./attempts.txt') as f:
        lines = [x.strip() for x in f.readlines()]
        occurences = { '0': dict(), '1': dict(), '2': dict(), '3': dict(), '4': dict(), '5': dict(), '6': dict(), '7': dict(), '8': dict(), '9': dict()}
        existingDigits = set()

        for code in lines:
            for digit in code:
                existingDigits.add(digit)

            if (not code[1] in occurences[code[0]]):
                occurences[code[0]][code[1]] = 1
            else:
                occurences[code[0]][code[1]] += 1

            if (not code[2] in occurences[code[1]]):
                occurences[code[1]][code[2]] = 1
            else:
                occurences[code[1]][code[2]] += 1

        # for k in occurences:
            # print(k, occurences[k])

        G = nx.DiGraph()
        G.add_nodes_from(existingDigits);

        for digit in existingDigits:
            G.add_edges_from([(digit, dest) for dest in occurences[digit]])

        res = []
        for node in G.nodes():
            res.append((node, [s for s in G.successors(node)]))

        res.sort(key=lambda a : len(a[1]))
        for node in res:
            print(node)

        # Following the successors lists manually, beginning
        # from the node with zero successors and going up to the ones
        # with more and more successor we can find the solution manually
        # Now I'll have to figure out how to find the result programatically

main()
