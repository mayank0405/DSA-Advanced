#Undirected Graph
from typing import List
from collections import defaultdict
def graph(n: int, m: int, edgeList: List[List[int]]):
    adj = defaultdict(list)
    for u, v in edgeList:
        adj[u].append(v)
        adj[v].append(u)

    #represent graph in list
    ans = []
    for i in range(n): #for the ith vertex
        ans.append([i] + adj[i])
    
