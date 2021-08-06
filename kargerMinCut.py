'''
Created on July 7, 2021

@author: izakaria
'''

import random

# Load the file into a graph represented by a dict of lists
def loadGraph():
    data_set = {}

    with open('kargerMinCut.txt') as f:
        #kargerMinCut
        #a = [[int(x) for x in ln.split()] for ln in f]
        for ln in f:
            line = ln.split()
            if line:
                a = [int(x) for x in line]
                data_set[a[0]]= a[1:]
    
    return data_set

# Contract an edge between 2 vertices
def contractEdge(edge):
    global dataG 
    
    # merge v2 into v1 and remove v2 from graph
    v1l = dataG[edge[0]]
    print (v1l)
    print (edge[1])
    print (dataG[edge[1]])
    v1l.extend(dataG[edge[1]])
    del dataG[edge[1]]
    
    #replace all occurnces of v2 value with v1
    for keyVertice in dataG:
        dataG[keyVertice] = [edge[0] if x == edge[1] else x for x in dataG[keyVertice]]
    
    # Remove all edges of v1 to itself(loops)
    dataG[edge[0]] = [x for x in dataG[edge[0]] if x != edge[0]]
    
# Get two random vertices
def getRandomEdge():
    global dataG
    
    v1 = random.choice(list(dataG))
    v2 = random.choice(dataG[v1])
    return (v1,v2)

if __name__ == '__main__':
    
    minlist = []
        
    for i in range(0,20):
        print(i)
        dataG = loadGraph()
        # Keep contracting the graph until we have 2 vertices
        while(len(dataG) > 2):
            contractEdge(getRandomEdge())
        
        firstkey = list(dataG.keys())[0]
        firstkey = list(dataG.keys())[0]
        minlist.append(len(dataG[firstkey]))
    print("minlist=  ", minlist)
    print (min(minlist))
    pass

