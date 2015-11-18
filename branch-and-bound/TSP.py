#! /usr/bin/python

from Graph import Graph
from Queue import PriorityQueue
import copy
import time
import sys

class TS(object):
    def __init__(self, graph):
        self.graph = graph

    def addNode(self, dest, currentPath):
        pathLen = len(currentPath)
        distance = 0
        if pathLen > 0:
            distance = self.graph.getPathLength(currentPath) + self.graph.distance(currentPath[pathLen - 1], dest)
        currentPath.append(dest)
        return (self.graph.upperBound(distance, currentPath), currentPath)

    def travel(self):
        visitedNodes = 0
        optimalPath = []
        priorityQueue = PriorityQueue()
        optimalPathLen = -1
        priorityQueue.put(self.addNode(0, []))
        startTime = time.time()
        while not priorityQueue.empty():
            currentPath = priorityQueue.get()[1]
            if optimalPath:
                pathLen = self.graph.getPathLength(optimalPath)
                upperBound = self.graph.upperBound(self.graph.getPathLength(currentPath), currentPath)
                optimalPathLen = self.graph.getPathLength(optimalPath)
            # Jesli nie mamy sciezki lub jest ona gorsza od UB
            if not optimalPath or upperBound < pathLen:
                visitedNodes += 1
                # Jesli odwiedzono wszystkie miasta
                if len(currentPath) >= self.graph.size:
                    # Jesli mozna wrocic do miasta poczatkowego z ostatniego punktu sciezki
                    if(self.graph.distance(currentPath[len(currentPath)-1], 0) > 0):
                        currentPath = self.addNode(0, currentPath)[1]
                        # Jesli nie mamy sciezki lub zmodyfikowan jest lepsza niz dotychczasowe
                        if not optimalPath or optimalPathLen > self.graph.getPathLength(currentPath):
                            optimalPath = currentPath
                else:
                    for i in range(self.graph.size):
                        # Jesli rozwazane miasto nie bylo odwiedzone i istnieje prowadzaca do niego droga
                        if i not in currentPath and self.graph.distance(currentPath[len(currentPath)-1], i)>0:
                            newPath = copy.deepcopy(currentPath)
                            bound, newPath = self.addNode(i, newPath)
                            if not optimalPath or bound < optimalPathLen:
                                priorityQueue.put((bound, newPath))
        return [optimalPath, self.graph.getPathLength(optimalPath), visitedNodes, time.time() - startTime]


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print """
        Too few arguments\n
        Usage:\n
        print 'python {0} -f filename.xml\n
        print 'python {0} numberOfPlaces\n
        """.format(sys.argv[0])
        sys.exit()
    if sys.argv[1] != '-f':
        aGraph = Graph(int(sys.argv[1]), 1, 100)

    else:
        aGraph = Graph()
        aGraph.parseTSPxml(sys.argv[2])
    print aGraph   
     
    ts = TS(aGraph)    
    (path, length, nodes, elapsedTime) = ts.travel()
    print 'Calculation took {0} seconds'.format(elapsedTime)
    print 'Visisted {0} nodes'.format(nodes)
    if path:
        print 'Shortest tour is {0} long:'.format(length)
        print path
    else:
        print 'No tour found'
    
