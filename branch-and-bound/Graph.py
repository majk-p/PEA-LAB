#!/usr/bin/python

import string
import random
import math
import xmltodict

class Graph:
    '''
    A simple class that represents a graph as an NxN matrix of numbers.
    The graph also includes a list of node "names" that are used to
    interpret the contents
    '''


    def __init__(self, size=0, density=0, maxDistance=0):
        if size < 1:
            pass
        self.size = size
        self.matrix = [[-1 for i in range(size)] for j in range(size)]

        density = density if density*100 in range(0, 100) else 1.0

        for i in range(size):
            for j in range(size):
                if i==j:
                    self.matrix[i][j] = 0
                    continue
                chance = random.uniform(1, maxDistance)
                if density > random.uniform(0, 1):
                    self.matrix[i][j] = random.uniform(1, maxDistance)
                    self.matrix[j][i] = self.matrix[i][j]
                else:
                    self.matrix[i][j], self.matrix[j][i] = [-1,-1]   

    def getMatrix(self):
        '''
        Return our matrix attribute
        '''
        return self.matrix

    def distance(self, i, j):
        if i in range(self.size) and j in range(self.size):
            return self.matrix[i][j]
        return -1

    def getPathLength(self, path):
        dist = 0
        for i in range(len(path)-1):
            dist += self.distance(path[i], path[i+1])
        return dist

    def upperBound(self, currentDistance, visited):
        bound = currentDistance
        for i in range(self.size):
            shortest = -1
            for j in range(self.size):
                if i==j:
                    continue
                if j not in visited:
                    dist = self.distance(i, j)
                    if shortest == -1 or (dist < shortest and dist > -1):
                        shortest = dist
            bound += currentDistance
        return bound

    def parseTSPxml(self, filename):
        with open(filename) as f:
            vertexIdx = 0
            data = xmltodict.parse(f.read())['travellingSalesmanProblemInstance'] 
            self.size = len(data['graph']['vertex'])
            self.matrix = [[0 for i in range(self.size)] for j in range(self.size)]
            for vertex in data['graph']['vertex']:
                for edge in vertex['edge']:                    
                    target = int(edge['#text'])
                    if target == vertexIdx:
                        self.matrix[vertexIdx][target] = 0
                    else:
                        self.matrix[vertexIdx][target] = float(edge['@cost'])
                    self.matrix[target][vertexIdx] = self.matrix[vertexIdx][target]
                vertexIdx += 1


    def __str__(self):
        ret = ""
        for row in self.matrix:
            ret += " ".join("{:8.3f}".format(i) for i in row) + "\n"

        return ret

def testDemo():
    newGraph = Graph(10, 0.6, 1000)
    print newGraph
    newGraph.parseTSPxml('ulysses16.xml')
    print newGraph

if (__name__ == '__main__'):
    testDemo()
