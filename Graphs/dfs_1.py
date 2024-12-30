from typing import List
def DFS(V: int, E: int, edges: List[List[int]]) -> List[int]:
    adj = [ [] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    stack = []
    ans = []
    visited = [False]*V
    stack.append(0)
    visited[0] = True
    while stack:
        node = stack.pop()
        ans.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                stack.append(neighbor)
                visited[node] = True
    
    return ans