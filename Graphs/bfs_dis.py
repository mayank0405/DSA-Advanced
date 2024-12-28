from typing import List
from collections import deque


def bfs(adj: List[List[int]], visited: List[int], s: int)-> None:
    pass


def bfs_dis(adj: List[List[int]]) -> List[int]:
    n = len(adj)
    visited = [False] * n
    ans = []
    for i in range(n):
        if not visited[i]:
            bfs(adj, visited, i)