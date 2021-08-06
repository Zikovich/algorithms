'''
Created on July 30, 2021
@author: izakaria
'''

import sys
import resource

# to increase stack of python to avoid max recursion 
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))


def dfsRev(graph , node):
    global finishingTime
    global explored
    global finish
    explored.add(node)
    for edge in graph[node]:
        if edge not in explored:
            dfsRev(graph , edge)
    finish += 1
    finishingTime[node] = finish
    
def dfsLoopRev(graphRev):
    global explored
    for node in reversed(list(graphRev.keys())):
        if node not in explored:
            dfsRev(graphRev , node)


def dfs(graph , node):
    global SCCs
    global explored
    global leaderVertix
    explored.add(node)    
    for edge in graph[node]:
        if edge not in explored:
            dfs(graph,edge)
            SCCs[leaderVertix] += 1
        
def dfsLoop(graph):
    global explored
    global SCCs
    explored.clear()
    global finishingTime
    global leaderVertix
    f_time = sorted(list(graph.keys()), key = lambda f_time : finishingTime[f_time],reverse=True)
    for node in f_time:
        if node not in explored:
            leaderVertix = node
            SCCs[leaderVertix] = 1
            dfs(graph , node)
            
if __name__ == '__main__':
    
	# global parameter
	explored = set()
	leaderVertix = None
	finishingTime = {} 
	SCCs = {}
	finish = 0
	
    # read Graph
	Graph = {}
	GraphRev = {}
	with open('SCC.txt') as f:
		for ln in f:
			if len(ln) >1:
				u,v = ln.split()
			try:
				(Graph[u]).append(v)
			except KeyError:
				Graph[str(u)] = [v]
			try:
				(GraphRev[v]).append(u)
			except KeyError:
				GraphRev[str(v)] = [u]
			if u not in GraphRev.keys():
				GraphRev[str(u)] = []
			if v not in Graph.keys():
				Graph[str(v)] = []
        
	f.close()

    
	# calculate DFS for G reversed
	dfsLoopRev(GraphRev)
    
	# calculate DFS for G given finished time 
	dfsLoop(Graph)

	#Select first max 5 from leaders

	ans = ""
	sccs = sorted(list(SCCs.values()), reverse =True) 

	for i in range(5):
		try:
			ans += str(sccs[i])
		except IndexError:
			ans+= "0"
		if i < 4:
			ans +=","
		
	print(ans)
